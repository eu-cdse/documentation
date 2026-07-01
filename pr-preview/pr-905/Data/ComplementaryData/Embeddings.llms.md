# Global Embeddings Dataset

The Global Embeddings Dataset represents a dense, large-scale collection of satellite image embeddings derived from the Major TOM Core datasets: Major-TOM/Core-S2L1C, Major-TOM/Core-S2L2A, and Major-TOM/Core-S1RTC (Francis and Czerkawski, 2024). These datasets provide access to over 60 TB of AI-ready Copernicus data with multiple sensing modalities, including multi-spectral (MSI), true-color RGB, and Synthetic Aperture Radar (SAR), at various processing levels.

## Source Datasets and Preprocessing

1.  Major-TOM/Core-S2L1C - Sentinel-2 Level 1C imagery, multi-spectral (10 m resolution)
2.  Major-TOM/Core-S2L2A - Sentinel-2 Level 2A imagery, true-color and multi-spectral
3.  Major-TOM/Core-S1RTC - Sentinel-1 Radiometrically Terrain Corrected (RTC) SAR products

Each image covers 10.68 × 10.68 km, corresponding to 1,068 × 1,068 pixels at 10 m resolution, representing a complete Major TOM grid cell plus margins. Since most pre-trained deep neural networks require smaller inputs (commonly 224×224 pixels), the images are fragmented into tiles. This fragmentation process avoids excessive information loss from resizing, which is critical in remote sensing applications where fine spatial details are essential.

## Embeddings Generation

Embeddings are computed using state-of-the-art (SOTA) self-supervised and supervised models:

| Dataset | Modality | Number of Embeddings | Sensing Type | Source Dataset | Source Model | Size |
|:--:|:--:|:--:|:--:|:--:|:--:|:--:|
| Core-S2L1C-SSL4EO | Sentinel-2 Level 1C | 56,147,150 | Multi-Spectral | Core-S2L1C | SSL4EO-ResNet50-DINO | 252.9 GB |
| Core-S1RTC-SSL4EO | Sentinel-1 RTC | 36,748,875 | SAR | Core-S1RTC | SSL4EO-ResNet50-MOCO | 332.5 GB |
| Core-S2RGB-DINOv2 | Sentinel-2 Level 2A (RGB) | 56,147,150 | True Colour | Core-S2L2A | DINOv2 | 223.1 GB |
| Core-S2RGB-SigLIP | Sentinel-2 Level 2A (RGB) | 20,212,974 | True Colour | Core-S2L2A | SigLIP-SO400M-384 | 41.3 GB |
| Core-S2L1C-DeCUR | Sentinel-2 Level 1C | 56,147,150 | Multi-Spectral | Core-S2L1C | SSL4EO-ResNet50-DeCUR | 252.9 GB |
| Core-S1RTC-DeCUR | Sentinel-1 RTC | 36,748,875 | SAR | Core-S1RTC | SSL4EO-ResNet50-DeCUR | 332.5 GB |
| Core-S2L2A-MMEarth | Sentinel-2 Level 2A (MSI) | 39,727,477,454 | Multi-Spectral | Core-S2L2A | MMEarth | 60 TB |

These embeddings represent high-dimensional latent vectors capturing the spectral, spatial, and contextual characteristics of each image fragment.

## Data Storage and Structure

Embeddings and metadata are stored in GeoParquet files, which extend standard Parquet by supporting geometry-type columns while retaining columnar efficiency, compression, and interoperability with geospatial pipelines. Each record includes:

| Field | Type | Description |
|:--:|:--:|:---|
| unique_id | string | hash generated from geometry, time, product_id, and embeddings model |
| embeddings | array | raw embeddings array |
| grid_cell | string | Major TOM cell |
| grid_row_u | int | Major TOM cell row |
| grid_col_r | int | Major TOM cell col |
| product_id | string | ID of the original product |
| timestamp | string | Timestamp of the sample |
| centre_lat | float | Centre of the fragment latitude |
| centre_lon | float | Centre of the fragment longitude |
| geometry | geometry | Polygon footprint (WGS84) of the fragment |
| utm_footprint | string | Polygon footprint (image UTM) of the fragment |
| utm_crs | string | CRS of the original product |
| pixel_bbox | bbox | Boundary box of the fragment (pixels) |

## Public Access via S3

The embeddings are available on EODATA S3 for direct download and integration into machine learning workflows:

- s3://EODATA/auxdata/MajorTOM/embeddings/Core-S1RTC-DeCUR/
- s3://EODATA/auxdata/MajorTOM/embeddings/Core-S1RTC-SSL4EO/
- s3://EODATA/auxdata/MajorTOM/embeddings/Core-S2L1C-DeCUR/
- s3://EODATA/auxdata/MajorTOM/embeddings/Core-S2L1C-SSL4EO/
- s3://EODATA/auxdata/MajorTOM/embeddings/Core-S2L2A-MMEarth/
- s3://EODATA/auxdata/MajorTOM/embeddings/Core-S2RGB-DINOv2/
- s3://EODATA/auxdata/MajorTOM/embeddings/Core-S2RGB-SigLIP/

Each path corresponds to a specific source dataset, sensing modality, and pre-trained model, enabling tailored selection of embeddings depending on application needs.

## Use Cases and Applications

The Major TOM embeddings datasets are designed for large-scale geospatial machine learning tasks, including but not limited to:

- Semantic segmentation and classification of land cover and land use.
- Change detection over time for environmental monitoring.
- Multi-modal data fusion leveraging combined SAR and optical data.
- Feature extraction for downstream AI models requiring compact, high-dimensional representations.

The integration of dense embeddings with comprehensive metadata ensures reproducibility, transparency, and reliable linkage between latent representations and their original geospatial context.

## Reference

Czerkawski, M., Kluczek, M., & Bojanowski, J. S. (2024). Global and Dense Embeddings of Earth: Major TOM Floating in the Latent Space. [arXiv:2412.05600](https://arxiv.org/abs/2412.05600).
