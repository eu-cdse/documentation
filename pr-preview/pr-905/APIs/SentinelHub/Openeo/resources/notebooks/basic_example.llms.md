``` python
# Import required packages
import openeo
from openeo.processes import process
```

## Login to Copernicus Dataspace: [link](https://identity.dataspace.copernicus.eu/auth/realms/CDSE/protocol/openid-connect/auth?client_id=cdse-public&response_type=code&scope=openid&redirect_uri=https%3A//dataspace.copernicus.eu/account/confirmed/1)

``` python
# Connect to the back-end
connection = openeo.connect("https://openeosh.dataspace.copernicus.eu/")
```

``` python
connection.authenticate_oidc()
```

    Authenticated using refresh token.

    <Connection to 'https://openeosh.dataspace.copernicus.eu/1.2' with OidcBearerAuth>

``` python
load2 = connection.load_collection(collection_id = "SENTINEL2_L1C_SENTINELHUB", spatial_extent = {"west": 14.503132250376241, "south": 45.98989222284457, "east": 14.578437275398317, "north": 46.04381770188389, "width": 1250, "height": 1250}, temporal_extent = ["2022-03-26T00:00:00Z", "2022-03-26T23:59:59Z"], bands = ["B02", "B03", "B04"])
```

``` python
def sAdj(x, context = None):
    divide2 = x / 3 # x / MaxR
    ar = process("clip", x = divide2, min = 0, max = 1) # ar
    
    mima = 0.13 / 3 # midR/maxR
    multiply1 = ar * (2 * mima -1) # (ar * (2 * midR/maxR - 1)
    divisor = multiply1 - mima # (ar * (2 * midR/maxR - 1) - midR/maxR)
    dividend = ar * (ar * mima - 1) # ar * (ar * (midR/maxR) - 1)

    adj = dividend / divisor # (ar * (ar * (midR/maxR) - 1)) / (ar * (2 * midR/maxR - 1) - midR/maxR)
    gOffPow = 0.01**2.3
    power1 = 1.1**2.3
    gOffRange = power1 - gOffPow # (1+gOff)^gamma - gOffPow
    
    subtract3 = (adj + 0.01)**2.3 - gOffPow # ((adj + gOff)^gamma)-gOffPow
    adjGamma = subtract3 / gOffRange # sAdj
    return adjGamma
```

``` python
def process1(data, context = None):
    arrayB2 = data[2] - 0.041
    arrayB3 = data[1] - 0.024
    arrayB4 = data[0] - 0.013
    array1 = process("array_create", data = [sAdj(arrayB2), sAdj(arrayB3), sAdj(arrayB4)])
    return array1
```

``` python
apply1 = load2.apply_dimension(dimension = "bands", process = process1)
```

``` python
def sRGB(x, context = None):
    accept = x * 12.92 # (12.92 * x)
    power1 = x**0.41666666666
    reject = power1 * 1.055 - 0.055  # 1.055 * x^0.41666666666
    
    lte2 = process("lte", x = x, y = 0.0031308) # c <= 0.0031308
    if1 = process("if", value = lte2, accept = accept, reject = reject)
    return if1
```

``` python
def satEnh(data, context = None):
    r = data[2] # r
    g = data[1] # g
    b = data[0] # b
    
    rsat = 6.5 * r # r * sat
    gsat = 6.5 * g # g * sat
    bsat = 6.5 * b # b* sat
    subtract3 = 1 - 1.3 # (1 - sat)
    
    sum = r + g + b # (r + g + b)
    avg = sum / 3 # (r + g + b)/3
    
    avgS = subtract3 * avg  # (1 - sat) * ((r + g + b) / 3.0) 
    sum1 = rsat + avgS # r * sat + avgS
    sum2 = gsat + avgS # g * sat + avgS
    sum3 = bsat + avgS # b * sat + avgS
    
    clip1 = process("clip", x = sum1, min = 0, max = 1) # clip(avgS + r * sat)
    clip2 = process("clip", x = sum2, min = 0, max = 1) # clip(avgS + g * sat)
    clip3 = process("clip", x = sum3, min = 0, max = 1) # clip(avgS + b * sat)
    
    # satEnh(sAdj(smp.B04), sAdj(smp.B03), sAdj(smp.B02))
    array1 = process("array_create", data = [sRGB(clip1), sRGB(clip2), sRGB(clip3)])
    return array1
```

``` python
# satEnh
apply2 = apply1.apply_dimension(dimension = "bands", process = satEnh)
```

``` python
save5 = apply2.save_result(format = "jpeg")
```

``` python
print(save5.to_json())
```

    {
      "process_graph": {
        "loadcollection1": {
          "process_id": "load_collection",
          "arguments": {
            "bands": [
              "B02",
              "B03",
              "B04"
            ],
            "id": "SENTINEL2_L1C_SENTINELHUB",
            "spatial_extent": {
              "west": 14.503132250376241,
              "south": 45.98989222284457,
              "east": 14.578437275398317,
              "north": 46.04381770188389,
              "width": 1250,
              "height": 1250
            },
            "temporal_extent": [
              "2022-03-26T00:00:00Z",
              "2022-03-26T23:59:59Z"
            ]
          }
        },
        "applydimension1": {
          "process_id": "apply_dimension",
          "arguments": {
            "data": {
              "from_node": "loadcollection1"
            },
            "dimension": "bands",
            "process": {
              "process_graph": {
                "arrayelement1": {
                  "process_id": "array_element",
                  "arguments": {
                    "data": {
                      "from_parameter": "data"
                    },
                    "index": 2
                  }
                },
                "subtract1": {
                  "process_id": "subtract",
                  "arguments": {
                    "x": {
                      "from_node": "arrayelement1"
                    },
                    "y": 0.041
                  }
                },
                "divide1": {
                  "process_id": "divide",
                  "arguments": {
                    "x": {
                      "from_node": "subtract1"
                    },
                    "y": 3
                  }
                },
                "clip1": {
                  "process_id": "clip",
                  "arguments": {
                    "max": 1,
                    "min": 0,
                    "x": {
                      "from_node": "divide1"
                    }
                  }
                },
                "multiply1": {
                  "process_id": "multiply",
                  "arguments": {
                    "x": {
                      "from_node": "clip1"
                    },
                    "y": 0.043333333333333335
                  }
                },
                "subtract2": {
                  "process_id": "subtract",
                  "arguments": {
                    "x": {
                      "from_node": "multiply1"
                    },
                    "y": 1
                  }
                },
                "multiply2": {
                  "process_id": "multiply",
                  "arguments": {
                    "x": {
                      "from_node": "clip1"
                    },
                    "y": {
                      "from_node": "subtract2"
                    }
                  }
                },
                "multiply3": {
                  "process_id": "multiply",
                  "arguments": {
                    "x": {
                      "from_node": "clip1"
                    },
                    "y": -0.9133333333333333
                  }
                },
                "subtract3": {
                  "process_id": "subtract",
                  "arguments": {
                    "x": {
                      "from_node": "multiply3"
                    },
                    "y": 0.043333333333333335
                  }
                },
                "divide2": {
                  "process_id": "divide",
                  "arguments": {
                    "x": {
                      "from_node": "multiply2"
                    },
                    "y": {
                      "from_node": "subtract3"
                    }
                  }
                },
                "add1": {
                  "process_id": "add",
                  "arguments": {
                    "x": {
                      "from_node": "divide2"
                    },
                    "y": 0.01
                  }
                },
                "power1": {
                  "process_id": "power",
                  "arguments": {
                    "base": {
                      "from_node": "add1"
                    },
                    "p": 2.3
                  }
                },
                "subtract4": {
                  "process_id": "subtract",
                  "arguments": {
                    "x": {
                      "from_node": "power1"
                    },
                    "y": 2.5118864315095822e-05
                  }
                },
                "divide3": {
                  "process_id": "divide",
                  "arguments": {
                    "x": {
                      "from_node": "subtract4"
                    },
                    "y": 1.2450718500352103
                  }
                },
                "arrayelement2": {
                  "process_id": "array_element",
                  "arguments": {
                    "data": {
                      "from_parameter": "data"
                    },
                    "index": 1
                  }
                },
                "subtract5": {
                  "process_id": "subtract",
                  "arguments": {
                    "x": {
                      "from_node": "arrayelement2"
                    },
                    "y": 0.024
                  }
                },
                "divide4": {
                  "process_id": "divide",
                  "arguments": {
                    "x": {
                      "from_node": "subtract5"
                    },
                    "y": 3
                  }
                },
                "clip2": {
                  "process_id": "clip",
                  "arguments": {
                    "max": 1,
                    "min": 0,
                    "x": {
                      "from_node": "divide4"
                    }
                  }
                },
                "multiply4": {
                  "process_id": "multiply",
                  "arguments": {
                    "x": {
                      "from_node": "clip2"
                    },
                    "y": 0.043333333333333335
                  }
                },
                "subtract6": {
                  "process_id": "subtract",
                  "arguments": {
                    "x": {
                      "from_node": "multiply4"
                    },
                    "y": 1
                  }
                },
                "multiply5": {
                  "process_id": "multiply",
                  "arguments": {
                    "x": {
                      "from_node": "clip2"
                    },
                    "y": {
                      "from_node": "subtract6"
                    }
                  }
                },
                "multiply6": {
                  "process_id": "multiply",
                  "arguments": {
                    "x": {
                      "from_node": "clip2"
                    },
                    "y": -0.9133333333333333
                  }
                },
                "subtract7": {
                  "process_id": "subtract",
                  "arguments": {
                    "x": {
                      "from_node": "multiply6"
                    },
                    "y": 0.043333333333333335
                  }
                },
                "divide5": {
                  "process_id": "divide",
                  "arguments": {
                    "x": {
                      "from_node": "multiply5"
                    },
                    "y": {
                      "from_node": "subtract7"
                    }
                  }
                },
                "add2": {
                  "process_id": "add",
                  "arguments": {
                    "x": {
                      "from_node": "divide5"
                    },
                    "y": 0.01
                  }
                },
                "power2": {
                  "process_id": "power",
                  "arguments": {
                    "base": {
                      "from_node": "add2"
                    },
                    "p": 2.3
                  }
                },
                "subtract8": {
                  "process_id": "subtract",
                  "arguments": {
                    "x": {
                      "from_node": "power2"
                    },
                    "y": 2.5118864315095822e-05
                  }
                },
                "divide6": {
                  "process_id": "divide",
                  "arguments": {
                    "x": {
                      "from_node": "subtract8"
                    },
                    "y": 1.2450718500352103
                  }
                },
                "arrayelement3": {
                  "process_id": "array_element",
                  "arguments": {
                    "data": {
                      "from_parameter": "data"
                    },
                    "index": 0
                  }
                },
                "subtract9": {
                  "process_id": "subtract",
                  "arguments": {
                    "x": {
                      "from_node": "arrayelement3"
                    },
                    "y": 0.013
                  }
                },
                "divide7": {
                  "process_id": "divide",
                  "arguments": {
                    "x": {
                      "from_node": "subtract9"
                    },
                    "y": 3
                  }
                },
                "clip3": {
                  "process_id": "clip",
                  "arguments": {
                    "max": 1,
                    "min": 0,
                    "x": {
                      "from_node": "divide7"
                    }
                  }
                },
                "multiply7": {
                  "process_id": "multiply",
                  "arguments": {
                    "x": {
                      "from_node": "clip3"
                    },
                    "y": 0.043333333333333335
                  }
                },
                "subtract10": {
                  "process_id": "subtract",
                  "arguments": {
                    "x": {
                      "from_node": "multiply7"
                    },
                    "y": 1
                  }
                },
                "multiply8": {
                  "process_id": "multiply",
                  "arguments": {
                    "x": {
                      "from_node": "clip3"
                    },
                    "y": {
                      "from_node": "subtract10"
                    }
                  }
                },
                "multiply9": {
                  "process_id": "multiply",
                  "arguments": {
                    "x": {
                      "from_node": "clip3"
                    },
                    "y": -0.9133333333333333
                  }
                },
                "subtract11": {
                  "process_id": "subtract",
                  "arguments": {
                    "x": {
                      "from_node": "multiply9"
                    },
                    "y": 0.043333333333333335
                  }
                },
                "divide8": {
                  "process_id": "divide",
                  "arguments": {
                    "x": {
                      "from_node": "multiply8"
                    },
                    "y": {
                      "from_node": "subtract11"
                    }
                  }
                },
                "add3": {
                  "process_id": "add",
                  "arguments": {
                    "x": {
                      "from_node": "divide8"
                    },
                    "y": 0.01
                  }
                },
                "power3": {
                  "process_id": "power",
                  "arguments": {
                    "base": {
                      "from_node": "add3"
                    },
                    "p": 2.3
                  }
                },
                "subtract12": {
                  "process_id": "subtract",
                  "arguments": {
                    "x": {
                      "from_node": "power3"
                    },
                    "y": 2.5118864315095822e-05
                  }
                },
                "divide9": {
                  "process_id": "divide",
                  "arguments": {
                    "x": {
                      "from_node": "subtract12"
                    },
                    "y": 1.2450718500352103
                  }
                },
                "arraycreate1": {
                  "process_id": "array_create",
                  "arguments": {
                    "data": [
                      {
                        "from_node": "divide3"
                      },
                      {
                        "from_node": "divide6"
                      },
                      {
                        "from_node": "divide9"
                      }
                    ]
                  },
                  "result": true
                }
              }
            }
          }
        },
        "applydimension2": {
          "process_id": "apply_dimension",
          "arguments": {
            "data": {
              "from_node": "applydimension1"
            },
            "dimension": "bands",
            "process": {
              "process_graph": {
                "arrayelement4": {
                  "process_id": "array_element",
                  "arguments": {
                    "data": {
                      "from_parameter": "data"
                    },
                    "index": 2
                  }
                },
                "multiply10": {
                  "process_id": "multiply",
                  "arguments": {
                    "x": 6.5,
                    "y": {
                      "from_node": "arrayelement4"
                    }
                  }
                },
                "arrayelement5": {
                  "process_id": "array_element",
                  "arguments": {
                    "data": {
                      "from_parameter": "data"
                    },
                    "index": 1
                  }
                },
                "add4": {
                  "process_id": "add",
                  "arguments": {
                    "x": {
                      "from_node": "arrayelement4"
                    },
                    "y": {
                      "from_node": "arrayelement5"
                    }
                  }
                },
                "arrayelement6": {
                  "process_id": "array_element",
                  "arguments": {
                    "data": {
                      "from_parameter": "data"
                    },
                    "index": 0
                  }
                },
                "add5": {
                  "process_id": "add",
                  "arguments": {
                    "x": {
                      "from_node": "add4"
                    },
                    "y": {
                      "from_node": "arrayelement6"
                    }
                  }
                },
                "divide10": {
                  "process_id": "divide",
                  "arguments": {
                    "x": {
                      "from_node": "add5"
                    },
                    "y": 3
                  }
                },
                "multiply11": {
                  "process_id": "multiply",
                  "arguments": {
                    "x": -0.30000000000000004,
                    "y": {
                      "from_node": "divide10"
                    }
                  }
                },
                "add6": {
                  "process_id": "add",
                  "arguments": {
                    "x": {
                      "from_node": "multiply10"
                    },
                    "y": {
                      "from_node": "multiply11"
                    }
                  }
                },
                "clip4": {
                  "process_id": "clip",
                  "arguments": {
                    "max": 1,
                    "min": 0,
                    "x": {
                      "from_node": "add6"
                    }
                  }
                },
                "multiply12": {
                  "process_id": "multiply",
                  "arguments": {
                    "x": {
                      "from_node": "clip4"
                    },
                    "y": 12.92
                  }
                },
                "power4": {
                  "process_id": "power",
                  "arguments": {
                    "base": {
                      "from_node": "clip4"
                    },
                    "p": 0.41666666666
                  }
                },
                "multiply13": {
                  "process_id": "multiply",
                  "arguments": {
                    "x": {
                      "from_node": "power4"
                    },
                    "y": 1.055
                  }
                },
                "subtract13": {
                  "process_id": "subtract",
                  "arguments": {
                    "x": {
                      "from_node": "multiply13"
                    },
                    "y": 0.055
                  }
                },
                "lte1": {
                  "process_id": "lte",
                  "arguments": {
                    "x": {
                      "from_node": "clip4"
                    },
                    "y": 0.0031308
                  }
                },
                "if1": {
                  "process_id": "if",
                  "arguments": {
                    "accept": {
                      "from_node": "multiply12"
                    },
                    "reject": {
                      "from_node": "subtract13"
                    },
                    "value": {
                      "from_node": "lte1"
                    }
                  }
                },
                "multiply14": {
                  "process_id": "multiply",
                  "arguments": {
                    "x": 6.5,
                    "y": {
                      "from_node": "arrayelement5"
                    }
                  }
                },
                "add7": {
                  "process_id": "add",
                  "arguments": {
                    "x": {
                      "from_node": "multiply14"
                    },
                    "y": {
                      "from_node": "multiply11"
                    }
                  }
                },
                "clip5": {
                  "process_id": "clip",
                  "arguments": {
                    "max": 1,
                    "min": 0,
                    "x": {
                      "from_node": "add7"
                    }
                  }
                },
                "multiply15": {
                  "process_id": "multiply",
                  "arguments": {
                    "x": {
                      "from_node": "clip5"
                    },
                    "y": 12.92
                  }
                },
                "power5": {
                  "process_id": "power",
                  "arguments": {
                    "base": {
                      "from_node": "clip5"
                    },
                    "p": 0.41666666666
                  }
                },
                "multiply16": {
                  "process_id": "multiply",
                  "arguments": {
                    "x": {
                      "from_node": "power5"
                    },
                    "y": 1.055
                  }
                },
                "subtract14": {
                  "process_id": "subtract",
                  "arguments": {
                    "x": {
                      "from_node": "multiply16"
                    },
                    "y": 0.055
                  }
                },
                "lte2": {
                  "process_id": "lte",
                  "arguments": {
                    "x": {
                      "from_node": "clip5"
                    },
                    "y": 0.0031308
                  }
                },
                "if2": {
                  "process_id": "if",
                  "arguments": {
                    "accept": {
                      "from_node": "multiply15"
                    },
                    "reject": {
                      "from_node": "subtract14"
                    },
                    "value": {
                      "from_node": "lte2"
                    }
                  }
                },
                "multiply17": {
                  "process_id": "multiply",
                  "arguments": {
                    "x": 6.5,
                    "y": {
                      "from_node": "arrayelement6"
                    }
                  }
                },
                "add8": {
                  "process_id": "add",
                  "arguments": {
                    "x": {
                      "from_node": "multiply17"
                    },
                    "y": {
                      "from_node": "multiply11"
                    }
                  }
                },
                "clip6": {
                  "process_id": "clip",
                  "arguments": {
                    "max": 1,
                    "min": 0,
                    "x": {
                      "from_node": "add8"
                    }
                  }
                },
                "multiply18": {
                  "process_id": "multiply",
                  "arguments": {
                    "x": {
                      "from_node": "clip6"
                    },
                    "y": 12.92
                  }
                },
                "power6": {
                  "process_id": "power",
                  "arguments": {
                    "base": {
                      "from_node": "clip6"
                    },
                    "p": 0.41666666666
                  }
                },
                "multiply19": {
                  "process_id": "multiply",
                  "arguments": {
                    "x": {
                      "from_node": "power6"
                    },
                    "y": 1.055
                  }
                },
                "subtract15": {
                  "process_id": "subtract",
                  "arguments": {
                    "x": {
                      "from_node": "multiply19"
                    },
                    "y": 0.055
                  }
                },
                "lte3": {
                  "process_id": "lte",
                  "arguments": {
                    "x": {
                      "from_node": "clip6"
                    },
                    "y": 0.0031308
                  }
                },
                "if3": {
                  "process_id": "if",
                  "arguments": {
                    "accept": {
                      "from_node": "multiply18"
                    },
                    "reject": {
                      "from_node": "subtract15"
                    },
                    "value": {
                      "from_node": "lte3"
                    }
                  }
                },
                "arraycreate2": {
                  "process_id": "array_create",
                  "arguments": {
                    "data": [
                      {
                        "from_node": "if1"
                      },
                      {
                        "from_node": "if2"
                      },
                      {
                        "from_node": "if3"
                      }
                    ]
                  },
                  "result": true
                }
              }
            }
          }
        },
        "saveresult1": {
          "process_id": "save_result",
          "arguments": {
            "data": {
              "from_node": "applydimension2"
            },
            "format": "jpeg",
            "options": {}
          },
          "result": true
        }
      }
    }

``` python
save5.download("niceColor.jpeg")
```

``` python
from IPython.display import Image
Image(filename='niceColor.jpeg') 
```

![](basic_example_files/figure-html/cell-15-output-1.jpeg)
