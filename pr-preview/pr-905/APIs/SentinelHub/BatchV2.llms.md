# Batch Processing V2 API

**The BatchV2 API is only available for users with Copernicus Service user Accounts.** Please see eligibility criteria in [Which entities are qualified to get higher quotas in scope of “Copernicus Services” group and how can one ask for it?](https://documentation.dataspace.copernicus.eu/FAQ.html#which-entities-are-qualified-to-get-higher-quotas-in-scope-of-copernicus-services-group-and-how-can-one-ask-for-it) on user Account types and accordingly if eligible submit the [Change your Copernicus user type form](https://dataspace.copernicus.eu/copernicus-services-user).

## Overview

**BatchV2 Processing API** (or shortly "**BatchV2 API**") enables you to request data for large areas and/or longer time periods for any Sentinel Hub supported collection, including BYOC (bring your own data). It is an asynchronous REST service, meaning data won't be returned immediately but delivered to your specified object storage instead.

### Workflow

The Batch V2 Processing API comes with the set of REST APIs which support the execution of various workflows. The diagram below shows all possible statuses of a batch task:

- `CREATED`
- `ANALYSING`
- `ANALYSIS_DONE`
- `PROCESSING`
- `DONE`
- `FAILED`
- `STOPPED`

and user's actions:

- `ANALYSE`
- `START`
- `STOP`

which trigger transitions among them.

![](data:image/svg+xml;base64,PHN2ZyBpZD0ibWVybWFpZC0xNzI4OTk5MjIyNzg0IiB3aWR0aD0iMTAwJSIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIiBjbGFzcz0ic3RhdGVkaWFncmFtIiBoZWlnaHQ9IjY5OCIgc3R5bGU9Im1heC13aWR0aDo4NjYuNTQzOTQ1MzEyNXB4IiB2aWV3Ym94PSIwIDAgNDk1LjE2Nzk2ODc1IDY5OCI+PGc+PGRlZnM+PG1hcmtlciBpZD0ic3RhdGVkaWFncmFtLWJhcmJFbmQiIHJlZng9IjE5IiByZWZ5PSI3IiBtYXJrZXJ3aWR0aD0iMjAiIG1hcmtlcmhlaWdodD0iMTQiIG1hcmtlcnVuaXRzPSJzdHJva2VXaWR0aCIgb3JpZW50PSJhdXRvIj48cGF0aCBkPSJNIDE5LDcgTDksMTMgTDE0LDcgTDksMSBaIiAvPjwvbWFya2VyPjwvZGVmcz48ZyBjbGFzcz0icm9vdCI+PGcgY2xhc3M9ImNsdXN0ZXJzIj48L2c+PGcgY2xhc3M9ImVkZ2VQYXRocyI+PHBhdGggZD0iTTI2Ny45NzI2NTYyNSwyMkwyNjcuOTcyNjU2MjUsMjYuMTY2NjY2NjY2NjY2NjY4QzI2Ny45NzI2NTYyNSwzMC4zMzMzMzMzMzMzMzMzMzIsMjY3Ljk3MjY1NjI1LDM4LjY2NjY2NjY2NjY2NjY2NCwyNjcuOTcyNjU2MjUsNDdDMjY3Ljk3MjY1NjI1LDU1LjMzMzMzMzMzMzMzMzMzNiwyNjcuOTcyNjU2MjUsNjMuNjY2NjY2NjY2NjY2NjY0LDI2Ny45NzI2NTYyNSw2Ny44MzMzMzMzMzMzMzMzM0wyNjcuOTcyNjU2MjUsNzIiIGlkPSJlZGdlMCIgY2xhc3M9ImVkZ2UtdGhpY2tuZXNzLW5vcm1hbCB0cmFuc2l0aW9uIiBzdHlsZT0iZmlsbDpub25lIiBtYXJrZXItZW5kPSJ1cmwoI3N0YXRlZGlhZ3JhbS1iYXJiRW5kKSIgLz48cGF0aCBkPSJNMjY3Ljk3MjY1NjI1LDEwNUwyNjcuOTcyNjU2MjUsMTEwLjY2NjY2NjY2NjY2NjY3QzI2Ny45NzI2NTYyNSwxMTYuMzMzMzMzMzMzMzMzMzMsMjY3Ljk3MjY1NjI1LDEyNy42NjY2NjY2NjY2NjY2NywyNjcuOTcyNjU2MjUsMTM5QzI2Ny45NzI2NTYyNSwxNTAuMzMzMzMzMzMzMzMzMzQsMjY3Ljk3MjY1NjI1LDE2MS42NjY2NjY2NjY2NjY2NiwyNjcuOTcyNjU2MjUsMTY3LjMzMzMzMzMzMzMzMzM0TDI2Ny45NzI2NTYyNSwxNzMiIGlkPSJlZGdlMSIgY2xhc3M9ImVkZ2UtdGhpY2tuZXNzLW5vcm1hbCB0cmFuc2l0aW9uIiBzdHlsZT0iZmlsbDpub25lIiBtYXJrZXItZW5kPSJ1cmwoI3N0YXRlZGlhZ3JhbS1iYXJiRW5kKSIgLz48cGF0aCBkPSJNMjY3Ljk3MjY1NjI1LDIwNkwyNjcuOTcyNjU2MjUsMjEwLjE2NjY2NjY2NjY2NjY2QzI2Ny45NzI2NTYyNSwyMTQuMzMzMzMzMzMzMzMzMzQsMjY3Ljk3MjY1NjI1LDIyMi42NjY2NjY2NjY2NjY2NiwyNjcuOTcyNjU2MjUsMjMxQzI2Ny45NzI2NTYyNSwyMzkuMzMzMzMzMzMzMzMzMzQsMjY3Ljk3MjY1NjI1LDI0Ny42NjY2NjY2NjY2NjY2NiwyNjcuOTcyNjU2MjUsMjUxLjgzMzMzMzMzMzMzMzM0TDI2Ny45NzI2NTYyNSwyNTYiIGlkPSJlZGdlMiIgY2xhc3M9ImVkZ2UtdGhpY2tuZXNzLW5vcm1hbCB0cmFuc2l0aW9uIiBzdHlsZT0iZmlsbDpub25lIiBtYXJrZXItZW5kPSJ1cmwoI3N0YXRlZGlhZ3JhbS1iYXJiRW5kKSIgLz48cGF0aCBkPSJNMzA2LjcyMjY1NjI1LDI3MS44NTI4NTEzMjM4Mjg5M0wzMzAuOTUxODIyOTE2NjY2NywyNzYuMjk0MDQyNzY5ODU3NEMzNTUuMTgwOTg5NTgzMzMzMywyODAuNzM1MjM0MjE1ODg1OTUsNDAzLjYzOTMyMjkxNjY2NjcsMjg5LjYxNzYxNzEwNzk0Myw0MjcuODY4NDg5NTgzMzMzMywzMDAuOTc1NDc1MjIwNjM4MTVDNDUyLjA5NzY1NjI1LDMxMi4zMzMzMzMzMzMzMzMzLDQ1Mi4wOTc2NTYyNSwzMjYuMTY2NjY2NjY2NjY2Nyw0NTIuMDk3NjU2MjUsMzQwQzQ1Mi4wOTc2NTYyNSwzNTMuODMzMzMzMzMzMzMzMyw0NTIuMDk3NjU2MjUsMzY3LjY2NjY2NjY2NjY2NjcsNDUyLjA5NzY1NjI1LDM4MC4yMDgzMzMzMzMzMzMzQzQ1Mi4wOTc2NTYyNSwzOTIuNzUsNDUyLjA5NzY1NjI1LDQwNCw0NTIuMDk3NjU2MjUsNDE2Ljc1QzQ1Mi4wOTc2NTYyNSw0MjkuNSw0NTIuMDk3NjU2MjUsNDQzLjc1LDQ1Mi4wOTc2NTYyNSw0NTkuMjkxNjY2NjY2NjY2N0M0NTIuMDk3NjU2MjUsNDc0LjgzMzMzMzMzMzMzMzMsNDUyLjA5NzY1NjI1LDQ5MS42NjY2NjY2NjY2NjY3LDQ1Mi4wOTc2NTYyNSw1MDguNUM0NTIuMDk3NjU2MjUsNTI1LjMzMzMzMzMzMzMzMzQsNDUyLjA5NzY1NjI1LDU0Mi4xNjY2NjY2NjY2NjY2LDQ1Mi4wOTc2NTYyNSw1NTYuMjVDNDUyLjA5NzY1NjI1LDU3MC4zMzMzMzMzMzMzMzM0LDQ1Mi4wOTc2NTYyNSw1ODEuNjY2NjY2NjY2NjY2Niw0NTIuMDk3NjU2MjUsNTg3LjMzMzMzMzMzMzMzMzRMNDUyLjA5NzY1NjI1LDU5MyIgaWQ9ImVkZ2UzIiBjbGFzcz0iZWRnZS10aGlja25lc3Mtbm9ybWFsIHRyYW5zaXRpb24iIHN0eWxlPSJmaWxsOm5vbmUiIG1hcmtlci1lbmQ9InVybCgjc3RhdGVkaWFncmFtLWJhcmJFbmQpIiAvPjxwYXRoIGQ9Ik0yNTEuMDM1NzM0OTUzNzAzNywyNzMuNUwyNDIuOTcwNTM0MzM2NDE5NzUsMjc3LjY2NjY2NjY2NjY2NjdDMjM0LjkwNTMzMzcxOTEzNTgsMjgxLjgzMzMzMzMzMzMzMzMsMjE4Ljc3NDkzMjQ4NDU2NzksMjkwLjE2NjY2NjY2NjY2NjcsMjEwLjcwOTczMTg2NzI4Mzk1LDI5OC41QzIwMi42NDQ1MzEyNSwzMDYuODMzMzMzMzMzMzMzMywyMDIuNjQ0NTMxMjUsMzE1LjE2NjY2NjY2NjY2NjcsMjAyLjY0NDUzMTI1LDMxOS4zMzMzMzMzMzMzMzMzTDIwMi42NDQ1MzEyNSwzMjMuNSIgaWQ9ImVkZ2U0IiBjbGFzcz0iZWRnZS10aGlja25lc3Mtbm9ybWFsIHRyYW5zaXRpb24iIHN0eWxlPSJmaWxsOm5vbmUiIG1hcmtlci1lbmQ9InVybCgjc3RhdGVkaWFncmFtLWJhcmJFbmQpIiAvPjxwYXRoIGQ9Ik0xODMuOTYwODkwNDM2NzQ2OTgsMzU2LjVMMTc5LjI0Mjc5OTMyMjI4OTEzLDM2MC42NjY2NjY2NjY2NjY3QzE3NC41MjQ3MDgyMDc4MzEzLDM2NC44MzMzMzMzMzMzMzMzLDE2NS4wODg1MjU5Nzg5MTU2NywzNzMuMTY2NjY2NjY2NjY2NywxNjAuMzcwNDM0ODY0NDU3ODIsMzgxLjVDMTU1LjY1MjM0Mzc1LDM4OS44MzMzMzMzMzMzMzMzLDE1NS42NTIzNDM3NSwzOTguMTY2NjY2NjY2NjY2NywxNTUuNjUyMzQzNzUsNDAyLjMzMzMzMzMzMzMzMzNMMTU1LjY1MjM0Mzc1LDQwNi41IiBpZD0iZWRnZTUiIGNsYXNzPSJlZGdlLXRoaWNrbmVzcy1ub3JtYWwgdHJhbnNpdGlvbiIgc3R5bGU9ImZpbGw6bm9uZSIgbWFya2VyLWVuZD0idXJsKCNzdGF0ZWRpYWdyYW0tYmFyYkVuZCkiIC8+PHBhdGggZD0iTTE0MC45MjI2OTczNjg0MjEwNCw0MjRMMTMxLjM4MzQ5NzgwNzAxNzUzLDQyOS42NjY2NjY2NjY2NjY3QzEyMS44NDQyOTgyNDU2MTQwMyw0MzUuMzMzMzMzMzMzMzMzMywxMDIuNzY1ODk5MTIyODA3MDEsNDQ2LjY2NjY2NjY2NjY2NjcsOTMuMjI2Njk5NTYxNDAzNSw0NThDODMuNjg3NSw0NjkuMzMzMzMzMzMzMzMzMyw4My42ODc1LDQ4MC42NjY2NjY2NjY2NjY3LDgzLjY4NzUsNDg2LjMzMzMzMzMzMzMzMzNMODMuNjg3NSw0OTIiIGlkPSJlZGdlNiIgY2xhc3M9ImVkZ2UtdGhpY2tuZXNzLW5vcm1hbCB0cmFuc2l0aW9uIiBzdHlsZT0iZmlsbDpub25lIiBtYXJrZXItZW5kPSJ1cmwoI3N0YXRlZGlhZ3JhbS1iYXJiRW5kKSIgLz48cGF0aCBkPSJNOTguNDEzNDQzNjg4MTE4ODIsNTI1TDEwMy40NzA4Mzg0OTAwOTkwMyw1MzAuNjY2NjY2NjY2NjY2NkMxMDguNTI4MjMzMjkyMDc5MjIsNTM2LjMzMzMzMzMzMzMzMzQsMTE4LjY0MzAyMjg5NjAzOTYxLDU0Ny42NjY2NjY2NjY2NjY2LDEzOC4wNzA0NjcyMDI5NzAzMiw1NTlDMTU3LjQ5NzkxMTUwOTkwMSw1NzAuMzMzMzMzMzMzMzMzNCwxODYuMjM4MDEwNTE5ODAxOTcsNTgxLjY2NjY2NjY2NjY2NjYsMjAwLjYwODA2MDAyNDc1MjUsNTg3LjMzMzMzMzMzMzMzMzRMMjE0Ljk3ODEwOTUyOTcwMjk4LDU5MyIgaWQ9ImVkZ2U3IiBjbGFzcz0iZWRnZS10aGlja25lc3Mtbm9ybWFsIHRyYW5zaXRpb24iIHN0eWxlPSJmaWxsOm5vbmUiIG1hcmtlci1lbmQ9InVybCgjc3RhdGVkaWFncmFtLWJhcmJFbmQpIiAvPjxwYXRoIGQ9Ik0xNzYuMzU5MjM3OTM4NTk2NSw0MjRMMTg5Ljc2OTQxNzAzMjE2MzcyLDQyOS42NjY2NjY2NjY2NjY3QzIwMy4xNzk1OTYxMjU3MzEsNDM1LjMzMzMzMzMzMzMzMzMsMjI5Ljk5OTk1NDMxMjg2NTUsNDQ2LjY2NjY2NjY2NjY2NjcsMjQzLjQxMDEzMzQwNjQzMjcyLDQ2MC43NUMyNTYuODIwMzEyNSw0NzQuODMzMzMzMzMzMzMzMywyNTYuODIwMzEyNSw0OTEuNjY2NjY2NjY2NjY2NywyNTYuODIwMzEyNSw1MDguNUMyNTYuODIwMzEyNSw1MjUuMzMzMzMzMzMzMzMzNCwyNTYuODIwMzEyNSw1NDIuMTY2NjY2NjY2NjY2NiwyNTYuODIwMzEyNSw1NTYuMjVDMjU2LjgyMDMxMjUsNTcwLjMzMzMzMzMzMzMzMzQsMjU2LjgyMDMxMjUsNTgxLjY2NjY2NjY2NjY2NjYsMjU2LjgyMDMxMjUsNTg3LjMzMzMzMzMzMzMzMzRMMjU2LjgyMDMxMjUsNTkzIiBpZD0iZWRnZTgiIGNsYXNzPSJlZGdlLXRoaWNrbmVzcy1ub3JtYWwgdHJhbnNpdGlvbiIgc3R5bGU9ImZpbGw6bm9uZSIgbWFya2VyLWVuZD0idXJsKCNzdGF0ZWRpYWdyYW0tYmFyYkVuZCkiIC8+PHBhdGggZD0iTTY4Ljk2MTU1NjMxMTg4MTE4LDUyNUw2My45MDQxNjE1MDk5MDA5OCw1MzAuNjY2NjY2NjY2NjY2NkM1OC44NDY3NjY3MDc5MjA3ODYsNTM2LjMzMzMzMzMzMzMzMzQsNDguNzMxOTc3MTAzOTYwMzksNTQ3LjY2NjY2NjY2NjY2NjYsNDMuNjc0NTgyMzAxOTgwMTk1LDU1OUMzOC42MTcxODc1LDU3MC4zMzMzMzMzMzMzMzM0LDM4LjYxNzE4NzUsNTgxLjY2NjY2NjY2NjY2NjYsMzguNjE3MTg3NSw1ODcuMzMzMzMzMzMzMzMzNEwzOC42MTcxODc1LDU5MyIgaWQ9ImVkZ2U5IiBjbGFzcz0iZWRnZS10aGlja25lc3Mtbm9ybWFsIHRyYW5zaXRpb24iIHN0eWxlPSJmaWxsOm5vbmUiIG1hcmtlci1lbmQ9InVybCgjc3RhdGVkaWFncmFtLWJhcmJFbmQpIiAvPjxwYXRoIGQ9Ik0yODcuNTI4MDc4NTg5MTA4OTMsNTkzTDI5OC4wNzQxODAwNzQyNTc0LDU4Ny4zMzMzMzMzMzMzMzM0QzMwOC42MjAyODE1NTk0MDU5NSw1ODEuNjY2NjY2NjY2NjY2NiwzMjkuNzEyNDg0NTI5NzAzLDU3MC4zMzMzMzMzMzMzMzM0LDM0MC4yNTg1ODYwMTQ4NTE0Niw1NTYuMjVDMzUwLjgwNDY4NzUsNTQyLjE2NjY2NjY2NjY2NjYsMzUwLjgwNDY4NzUsNTI1LjMzMzMzMzMzMzMzMzQsMzUwLjgwNDY4NzUsNTA4LjVDMzUwLjgwNDY4NzUsNDkxLjY2NjY2NjY2NjY2NjcsMzUwLjgwNDY4NzUsNDc0LjgzMzMzMzMzMzMzMzMsMzUwLjgwNDY4NzUsNDU5LjI5MTY2NjY2NjY2NjdDMzUwLjgwNDY4NzUsNDQzLjc1LDM1MC44MDQ2ODc1LDQyOS41LDM1MC44MDQ2ODc1LDQxNi43NUMzNTAuODA0Njg3NSw0MDQsMzUwLjgwNDY4NzUsMzkyLjc1LDMzNS45MjkxNjk4MDQyMTY5LDM4Mi45NTgzMzMzMzMzMzMzQzMyMS4wNTM2NTIxMDg0MzM3LDM3My4xNjY2NjY2NjY2NjY3LDI5MS4zMDI2MTY3MTY4Njc1LDM2NC44MzMzMzMzMzMzMzMzLDI3Ni40MjcwOTkwMjEwODQzLDM2MC42NjY2NjY2NjY2NjY3TDI2MS41NTE1ODEzMjUzMDEyLDM1Ni41IiBpZD0iZWRnZTEwIiBjbGFzcz0iZWRnZS10aGlja25lc3Mtbm9ybWFsIHRyYW5zaXRpb24iIHN0eWxlPSJmaWxsOm5vbmUiIG1hcmtlci1lbmQ9InVybCgjc3RhdGVkaWFncmFtLWJhcmJFbmQpIiAvPjxwYXRoIGQ9Ik0zOC42MTcxODc1LDYyNkwzOC42MTcxODc1LDYzMC4xNjY2NjY2NjY2NjY2QzM4LjYxNzE4NzUsNjM0LjMzMzMzMzMzMzMzMzQsMzguNjE3MTg3NSw2NDIuNjY2NjY2NjY2NjY2Niw3NS42ODc2MjQ0NTA3NTA0Myw2NTIuMDA1NDUzMjI2MDQ0N0MxMTIuNzU4MDYxNDAxNTAwODcsNjYxLjM0NDIzOTc4NTQyMjcsMTg2Ljg5ODkzNTMwMzAwMTc0LDY3MS42ODg0Nzk1NzA4NDU1LDIyMy45NjkzNzIyNTM3NTIxNCw2NzYuODYwNTk5NDYzNTU2OEwyNjEuMDM5ODA5MjA0NTAyNiw2ODIuMDMyNzE5MzU2MjY4MiIgaWQ9ImVkZ2UxMSIgY2xhc3M9ImVkZ2UtdGhpY2tuZXNzLW5vcm1hbCB0cmFuc2l0aW9uIiBzdHlsZT0iZmlsbDpub25lIiBtYXJrZXItZW5kPSJ1cmwoI3N0YXRlZGlhZ3JhbS1iYXJiRW5kKSIgLz48cGF0aCBkPSJNNDUyLjA5NzY1NjI1LDYyNkw0NTIuMDk3NjU2MjUsNjMwLjE2NjY2NjY2NjY2NjZDNDUyLjA5NzY1NjI1LDYzNC4zMzMzMzMzMzMzMzM0LDQ1Mi4wOTc2NTYyNSw2NDIuNjY2NjY2NjY2NjY2Niw0MjIuNTU5NTkyODY1Mzg4NTQsNjUxLjk2NjkwMDM1NzQwNzFDMzkzLjAyMTUyOTQ4MDc3NzEzLDY2MS4yNjcxMzQwNDgxNDczLDMzMy45NDU0MDI3MTE1NTQyLDY3MS41MzQyNjgwOTYyOTQ4LDMwNC40MDczMzkzMjY5NDI3NSw2NzYuNjY3ODM1MTIwMzY4NUwyNzQuODY5Mjc1OTQyMzMxMyw2ODEuODAxNDAyMTQ0NDQyMSIgaWQ9ImVkZ2UxMiIgY2xhc3M9ImVkZ2UtdGhpY2tuZXNzLW5vcm1hbCB0cmFuc2l0aW9uIiBzdHlsZT0iZmlsbDpub25lIiBtYXJrZXItZW5kPSJ1cmwoI3N0YXRlZGlhZ3JhbS1iYXJiRW5kKSIgLz48L2c+PGcgY2xhc3M9ImVkZ2VMYWJlbHMiPjxnIGNsYXNzPSJlZGdlTGFiZWwiPjxnIGNsYXNzPSJsYWJlbCIgdHJhbnNmb3JtPSJ0cmFuc2xhdGUoMCwgMCkiPjxyZWN0IHJ4PSIwIiByeT0iMCIgd2lkdGg9IjAiIGhlaWdodD0iMCIgLz48Zm9yZWlnbm9iamVjdCB3aWR0aD0iMCIgaGVpZ2h0PSIwIj48ZGl2IHhtbG5zPSJodHRwOi8vd3d3LnczLm9yZy8xOTk5L3hodG1sIiBzdHlsZT0iZGlzcGxheTppbmxpbmUtYmxvY2s7d2hpdGUtc3BhY2U6bm93cmFwIj48c3BhbiBjbGFzcz0iZWRnZUxhYmVsIj48L3NwYW4+PC9kaXY+PC9mb3JlaWdub2JqZWN0PjwvZz48L2c+PGcgY2xhc3M9ImVkZ2VMYWJlbCIgdHJhbnNmb3JtPSJ0cmFuc2xhdGUoMjY3Ljk3MjY1NjI1LCAxMzkpIj48ZyBjbGFzcz0ibGFiZWwiIHRyYW5zZm9ybT0idHJhbnNsYXRlKC0xMTIuNTIzNDM3NSwgLTkpIj48cmVjdCByeD0iMCIgcnk9IjAiIHdpZHRoPSIyMjUuMDQ2ODc1IiBoZWlnaHQ9IjE4IiAvPjxmb3JlaWdub2JqZWN0IHdpZHRoPSIyMjUuMDQ2ODc1IiBoZWlnaHQ9IjE4Ij48ZGl2IHhtbG5zPSJodHRwOi8vd3d3LnczLm9yZy8xOTk5L3hodG1sIiBzdHlsZT0iZGlzcGxheTppbmxpbmUtYmxvY2s7d2hpdGUtc3BhY2U6bm93cmFwIj48c3BhbiBjbGFzcz0iZWRnZUxhYmVsIj7wn5GkIFNUQVJUL0FOQUxZU0U8L3NwYW4+PC9kaXY+PC9mb3JlaWdub2JqZWN0PjwvZz48L2c+PGcgY2xhc3M9ImVkZ2VMYWJlbCI+PGcgY2xhc3M9ImxhYmVsIiB0cmFuc2Zvcm09InRyYW5zbGF0ZSgwLCAwKSI+PHJlY3Qgcng9IjAiIHJ5PSIwIiB3aWR0aD0iMCIgaGVpZ2h0PSIwIiAvPjxmb3JlaWdub2JqZWN0IHdpZHRoPSIwIiBoZWlnaHQ9IjAiPjxkaXYgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzE5OTkveGh0bWwiIHN0eWxlPSJkaXNwbGF5OmlubGluZS1ibG9jazt3aGl0ZS1zcGFjZTpub3dyYXAiPjxzcGFuIGNsYXNzPSJlZGdlTGFiZWwiPjwvc3Bhbj48L2Rpdj48L2ZvcmVpZ25vYmplY3Q+PC9nPjwvZz48ZyBjbGFzcz0iZWRnZUxhYmVsIj48ZyBjbGFzcz0ibGFiZWwiIHRyYW5zZm9ybT0idHJhbnNsYXRlKDAsIDApIj48cmVjdCByeD0iMCIgcnk9IjAiIHdpZHRoPSIwIiBoZWlnaHQ9IjAiIC8+PGZvcmVpZ25vYmplY3Qgd2lkdGg9IjAiIGhlaWdodD0iMCI+PGRpdiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMTk5OS94aHRtbCIgc3R5bGU9ImRpc3BsYXk6aW5saW5lLWJsb2NrO3doaXRlLXNwYWNlOm5vd3JhcCI+PHNwYW4gY2xhc3M9ImVkZ2VMYWJlbCI+PC9zcGFuPjwvZGl2PjwvZm9yZWlnbm9iamVjdD48L2c+PC9nPjxnIGNsYXNzPSJlZGdlTGFiZWwiPjxnIGNsYXNzPSJsYWJlbCIgdHJhbnNmb3JtPSJ0cmFuc2xhdGUoMCwgMCkiPjxyZWN0IHJ4PSIwIiByeT0iMCIgd2lkdGg9IjAiIGhlaWdodD0iMCIgLz48Zm9yZWlnbm9iamVjdCB3aWR0aD0iMCIgaGVpZ2h0PSIwIj48ZGl2IHhtbG5zPSJodHRwOi8vd3d3LnczLm9yZy8xOTk5L3hodG1sIiBzdHlsZT0iZGlzcGxheTppbmxpbmUtYmxvY2s7d2hpdGUtc3BhY2U6bm93cmFwIj48c3BhbiBjbGFzcz0iZWRnZUxhYmVsIj48L3NwYW4+PC9kaXY+PC9mb3JlaWdub2JqZWN0PjwvZz48L2c+PGcgY2xhc3M9ImVkZ2VMYWJlbCI+PGcgY2xhc3M9ImxhYmVsIiB0cmFuc2Zvcm09InRyYW5zbGF0ZSgwLCAwKSI+PHJlY3Qgcng9IjAiIHJ5PSIwIiB3aWR0aD0iMCIgaGVpZ2h0PSIwIiAvPjxmb3JlaWdub2JqZWN0IHdpZHRoPSIwIiBoZWlnaHQ9IjAiPjxkaXYgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzE5OTkveGh0bWwiIHN0eWxlPSJkaXNwbGF5OmlubGluZS1ibG9jazt3aGl0ZS1zcGFjZTpub3dyYXAiPjxzcGFuIGNsYXNzPSJlZGdlTGFiZWwiPjwvc3Bhbj48L2Rpdj48L2ZvcmVpZ25vYmplY3Q+PC9nPjwvZz48ZyBjbGFzcz0iZWRnZUxhYmVsIiB0cmFuc2Zvcm09InRyYW5zbGF0ZSg4My42ODc1LCA0NTgpIj48ZyBjbGFzcz0ibGFiZWwiIHRyYW5zZm9ybT0idHJhbnNsYXRlKC03My45ODQzNzUsIC05KSI+PHJlY3Qgcng9IjAiIHJ5PSIwIiB3aWR0aD0iMTQ3Ljk2ODc1IiBoZWlnaHQ9IjE4IiAvPjxmb3JlaWdub2JqZWN0IHdpZHRoPSIxNDcuOTY4NzUiIGhlaWdodD0iMTgiPjxkaXYgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzE5OTkveGh0bWwiIHN0eWxlPSJkaXNwbGF5OmlubGluZS1ibG9jazt3aGl0ZS1zcGFjZTpub3dyYXAiPjxzcGFuIGNsYXNzPSJlZGdlTGFiZWwiPvCfkaQgU1RBUlQ8L3NwYW4+PC9kaXY+PC9mb3JlaWdub2JqZWN0PjwvZz48L2c+PGcgY2xhc3M9ImVkZ2VMYWJlbCIgdHJhbnNmb3JtPSJ0cmFuc2xhdGUoMTI4Ljc1NzgxMjUsIDU1OSkiPjxnIGNsYXNzPSJsYWJlbCIgdHJhbnNmb3JtPSJ0cmFuc2xhdGUoLTcwLjE0MDYyNSwgLTkpIj48cmVjdCByeD0iMCIgcnk9IjAiIHdpZHRoPSIxNDAuMjgxMjUiIGhlaWdodD0iMTgiIC8+PGZvcmVpZ25vYmplY3Qgd2lkdGg9IjE0MC4yODEyNSIgaGVpZ2h0PSIxOCI+PGRpdiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMTk5OS94aHRtbCIgc3R5bGU9ImRpc3BsYXk6aW5saW5lLWJsb2NrO3doaXRlLXNwYWNlOm5vd3JhcCI+PHNwYW4gY2xhc3M9ImVkZ2VMYWJlbCI+8J+RpCBTVE9QPC9zcGFuPjwvZGl2PjwvZm9yZWlnbm9iamVjdD48L2c+PC9nPjxnIGNsYXNzPSJlZGdlTGFiZWwiIHRyYW5zZm9ybT0idHJhbnNsYXRlKDI1Ni44MjAzMTI1LCA1MDguNSkiPjxnIGNsYXNzPSJsYWJlbCIgdHJhbnNmb3JtPSJ0cmFuc2xhdGUoLTcwLjE0MDYyNSwgLTkpIj48cmVjdCByeD0iMCIgcnk9IjAiIHdpZHRoPSIxNDAuMjgxMjUiIGhlaWdodD0iMTgiIC8+PGZvcmVpZ25vYmplY3Qgd2lkdGg9IjE0MC4yODEyNSIgaGVpZ2h0PSIxOCI+PGRpdiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMTk5OS94aHRtbCIgc3R5bGU9ImRpc3BsYXk6aW5saW5lLWJsb2NrO3doaXRlLXNwYWNlOm5vd3JhcCI+PHNwYW4gY2xhc3M9ImVkZ2VMYWJlbCI+8J+RpCBTVE9QPC9zcGFuPjwvZGl2PjwvZm9yZWlnbm9iamVjdD48L2c+PC9nPjxnIGNsYXNzPSJlZGdlTGFiZWwiPjxnIGNsYXNzPSJsYWJlbCIgdHJhbnNmb3JtPSJ0cmFuc2xhdGUoMCwgMCkiPjxyZWN0IHJ4PSIwIiByeT0iMCIgd2lkdGg9IjAiIGhlaWdodD0iMCIgLz48Zm9yZWlnbm9iamVjdCB3aWR0aD0iMCIgaGVpZ2h0PSIwIj48ZGl2IHhtbG5zPSJodHRwOi8vd3d3LnczLm9yZy8xOTk5L3hodG1sIiBzdHlsZT0iZGlzcGxheTppbmxpbmUtYmxvY2s7d2hpdGUtc3BhY2U6bm93cmFwIj48c3BhbiBjbGFzcz0iZWRnZUxhYmVsIj48L3NwYW4+PC9kaXY+PC9mb3JlaWdub2JqZWN0PjwvZz48L2c+PGcgY2xhc3M9ImVkZ2VMYWJlbCIgdHJhbnNmb3JtPSJ0cmFuc2xhdGUoMzUwLjgwNDY4NzUsIDQ1OCkiPjxnIGNsYXNzPSJsYWJlbCIgdHJhbnNmb3JtPSJ0cmFuc2xhdGUoLTczLjk4NDM3NSwgLTkpIj48cmVjdCByeD0iMCIgcnk9IjAiIHdpZHRoPSIxNDcuOTY4NzUiIGhlaWdodD0iMTgiIC8+PGZvcmVpZ25vYmplY3Qgd2lkdGg9IjE0Ny45Njg3NSIgaGVpZ2h0PSIxOCI+PGRpdiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMTk5OS94aHRtbCIgc3R5bGU9ImRpc3BsYXk6aW5saW5lLWJsb2NrO3doaXRlLXNwYWNlOm5vd3JhcCI+PHNwYW4gY2xhc3M9ImVkZ2VMYWJlbCI+8J+RpCBTVEFSVDwvc3Bhbj48L2Rpdj48L2ZvcmVpZ25vYmplY3Q+PC9nPjwvZz48ZyBjbGFzcz0iZWRnZUxhYmVsIj48ZyBjbGFzcz0ibGFiZWwiIHRyYW5zZm9ybT0idHJhbnNsYXRlKDAsIDApIj48cmVjdCByeD0iMCIgcnk9IjAiIHdpZHRoPSIwIiBoZWlnaHQ9IjAiIC8+PGZvcmVpZ25vYmplY3Qgd2lkdGg9IjAiIGhlaWdodD0iMCI+PGRpdiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMTk5OS94aHRtbCIgc3R5bGU9ImRpc3BsYXk6aW5saW5lLWJsb2NrO3doaXRlLXNwYWNlOm5vd3JhcCI+PHNwYW4gY2xhc3M9ImVkZ2VMYWJlbCI+PC9zcGFuPjwvZGl2PjwvZm9yZWlnbm9iamVjdD48L2c+PC9nPjxnIGNsYXNzPSJlZGdlTGFiZWwiPjxnIGNsYXNzPSJsYWJlbCIgdHJhbnNmb3JtPSJ0cmFuc2xhdGUoMCwgMCkiPjxyZWN0IHJ4PSIwIiByeT0iMCIgd2lkdGg9IjAiIGhlaWdodD0iMCIgLz48Zm9yZWlnbm9iamVjdCB3aWR0aD0iMCIgaGVpZ2h0PSIwIj48ZGl2IHhtbG5zPSJodHRwOi8vd3d3LnczLm9yZy8xOTk5L3hodG1sIiBzdHlsZT0iZGlzcGxheTppbmxpbmUtYmxvY2s7d2hpdGUtc3BhY2U6bm93cmFwIj48c3BhbiBjbGFzcz0iZWRnZUxhYmVsIj48L3NwYW4+PC9kaXY+PC9mb3JlaWdub2JqZWN0PjwvZz48L2c+PC9nPjxnIGNsYXNzPSJub2RlcyI+PGcgY2xhc3M9Im5vZGUgZGVmYXVsdCIgaWQ9InN0YXRlLXJvb3Rfc3RhcnQtMCIgdHJhbnNmb3JtPSJ0cmFuc2xhdGUoMjY3Ljk3MjY1NjI1LCAxNSkiPjxjaXJjbGUgY2xhc3M9InN0YXRlLXN0YXJ0IiByPSI3IiB3aWR0aD0iMTQiIGhlaWdodD0iMTQiPjwvY2lyY2xlPjwvZz48ZyBjbGFzcz0ibm9kZSBzdGF0ZWRpYWdyYW0tc3RhdGUiIGlkPSJzdGF0ZS1DUkVBVEVELTEiIHRyYW5zZm9ybT0idHJhbnNsYXRlKDI2Ny45NzI2NTYyNSwgODguNSkiPjxyZWN0IGNsYXNzPSJiYXNpYyBsYWJlbC1jb250YWluZXIiIHg9Ii00NS4xMzI4MTI1IiB5PSItMTYuNSIgd2lkdGg9IjkwLjI2NTYyNSIgaGVpZ2h0PSIzMyIgLz48ZyBjbGFzcz0ibGFiZWwiIHRyYW5zZm9ybT0idHJhbnNsYXRlKC0zNy42MzI4MTI1LCAtOSkiPjxmb3JlaWdub2JqZWN0IHdpZHRoPSI3NS4yNjU2MjUiIGhlaWdodD0iMTgiPjxkaXYgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzE5OTkveGh0bWwiIHN0eWxlPSJkaXNwbGF5OmlubGluZS1ibG9jazt3aGl0ZS1zcGFjZTpub3dyYXAiPjxzcGFuIGNsYXNzPSJub2RlTGFiZWwiPkNSRUFURUQ8L3NwYW4+PC9kaXY+PC9mb3JlaWdub2JqZWN0PjwvZz48L2c+PGcgY2xhc3M9Im5vZGUgc3RhdGVkaWFncmFtLXN0YXRlIiBpZD0ic3RhdGUtQU5BTFlTSU5HLTIiIHRyYW5zZm9ybT0idHJhbnNsYXRlKDI2Ny45NzI2NTYyNSwgMTg5LjUpIj48cmVjdCBjbGFzcz0iYmFzaWMgbGFiZWwtY29udGFpbmVyIiB4PSItNTIuNzAzMTI1IiB5PSItMTYuNSIgd2lkdGg9IjEwNS40MDYyNSIgaGVpZ2h0PSIzMyIgLz48ZyBjbGFzcz0ibGFiZWwiIHRyYW5zZm9ybT0idHJhbnNsYXRlKC00NS4yMDMxMjUsIC05KSI+PGZvcmVpZ25vYmplY3Qgd2lkdGg9IjkwLjQwNjI1IiBoZWlnaHQ9IjE4Ij48ZGl2IHhtbG5zPSJodHRwOi8vd3d3LnczLm9yZy8xOTk5L3hodG1sIiBzdHlsZT0iZGlzcGxheTppbmxpbmUtYmxvY2s7d2hpdGUtc3BhY2U6bm93cmFwIj48c3BhbiBjbGFzcz0ibm9kZUxhYmVsIj5BTkFMWVNJTkc8L3NwYW4+PC9kaXY+PC9mb3JlaWdub2JqZWN0PjwvZz48L2c+PGcgY2xhc3M9Im5vZGUgZGVmYXVsdCIgaWQ9InN0YXRlLWZvcmtfc3RhdGVfYW5hbHlzaXMtNCIgdHJhbnNmb3JtPSJ0cmFuc2xhdGUoMjY3Ljk3MjY1NjI1LCAyNjQuNzUpIj48cmVjdCB4PSItMzUiIHk9Ii01IiB3aWR0aD0iNzAiIGhlaWdodD0iMTAiIGNsYXNzPSJmb3JrLWpvaW4iIC8+PC9nPjxnIGNsYXNzPSJub2RlIHN0YXRlZGlhZ3JhbS1zdGF0ZSIgaWQ9InN0YXRlLUZBSUxFRC0xMiIgdHJhbnNmb3JtPSJ0cmFuc2xhdGUoNDUyLjA5NzY1NjI1LCA2MDkuNSkiPjxyZWN0IGNsYXNzPSJiYXNpYyBsYWJlbC1jb250YWluZXIiIHg9Ii0zNS4wNzAzMTI1IiB5PSItMTYuNSIgd2lkdGg9IjcwLjE0MDYyNSIgaGVpZ2h0PSIzMyIgLz48ZyBjbGFzcz0ibGFiZWwiIHRyYW5zZm9ybT0idHJhbnNsYXRlKC0yNy41NzAzMTI1LCAtOSkiPjxmb3JlaWdub2JqZWN0IHdpZHRoPSI1NS4xNDA2MjUiIGhlaWdodD0iMTgiPjxkaXYgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzE5OTkveGh0bWwiIHN0eWxlPSJkaXNwbGF5OmlubGluZS1ibG9jazt3aGl0ZS1zcGFjZTpub3dyYXAiPjxzcGFuIGNsYXNzPSJub2RlTGFiZWwiPkZBSUxFRDwvc3Bhbj48L2Rpdj48L2ZvcmVpZ25vYmplY3Q+PC9nPjwvZz48ZyBjbGFzcz0ibm9kZSBzdGF0ZWRpYWdyYW0tc3RhdGUiIGlkPSJzdGF0ZS1BTkFMWVNJU19ET05FLTEwIiB0cmFuc2Zvcm09InRyYW5zbGF0ZSgyMDIuNjQ0NTMxMjUsIDM0MCkiPjxyZWN0IGNsYXNzPSJiYXNpYyBsYWJlbC1jb250YWluZXIiIHg9Ii03My42MDE1NjI1IiB5PSItMTYuNSIgd2lkdGg9IjE0Ny4yMDMxMjUiIGhlaWdodD0iMzMiIC8+PGcgY2xhc3M9ImxhYmVsIiB0cmFuc2Zvcm09InRyYW5zbGF0ZSgtNjYuMTAxNTYyNSwgLTkpIj48Zm9yZWlnbm9iamVjdCB3aWR0aD0iMTMyLjIwMzEyNSIgaGVpZ2h0PSIxOCI+PGRpdiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMTk5OS94aHRtbCIgc3R5bGU9ImRpc3BsYXk6aW5saW5lLWJsb2NrO3doaXRlLXNwYWNlOm5vd3JhcCI+PHNwYW4gY2xhc3M9Im5vZGVMYWJlbCI+QU5BTFlTSVNfRE9ORTwvc3Bhbj48L2Rpdj48L2ZvcmVpZ25vYmplY3Q+PC9nPjwvZz48ZyBjbGFzcz0ibm9kZSBkZWZhdWx0IiBpZD0ic3RhdGUtZm9ya19zdGF0ZV9hbmFseXNpc19kb25lLTgiIHRyYW5zZm9ybT0idHJhbnNsYXRlKDE1NS42NTIzNDM3NSwgNDE1LjI1KSI+PHJlY3QgeD0iLTM1IiB5PSItNSIgd2lkdGg9IjcwIiBoZWlnaHQ9IjEwIiBjbGFzcz0iZm9yay1qb2luIiAvPjwvZz48ZyBjbGFzcz0ibm9kZSBzdGF0ZWRpYWdyYW0tc3RhdGUiIGlkPSJzdGF0ZS1QUk9DRVNTSU5HLTkiIHRyYW5zZm9ybT0idHJhbnNsYXRlKDgzLjY4NzUsIDUwOC41KSI+PHJlY3QgY2xhc3M9ImJhc2ljIGxhYmVsLWNvbnRhaW5lciIgeD0iLTYwLjg0Mzc1IiB5PSItMTYuNSIgd2lkdGg9IjEyMS42ODc1IiBoZWlnaHQ9IjMzIiAvPjxnIGNsYXNzPSJsYWJlbCIgdHJhbnNmb3JtPSJ0cmFuc2xhdGUoLTUzLjM0Mzc1LCAtOSkiPjxmb3JlaWdub2JqZWN0IHdpZHRoPSIxMDYuNjg3NSIgaGVpZ2h0PSIxOCI+PGRpdiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMTk5OS94aHRtbCIgc3R5bGU9ImRpc3BsYXk6aW5saW5lLWJsb2NrO3doaXRlLXNwYWNlOm5vd3JhcCI+PHNwYW4gY2xhc3M9Im5vZGVMYWJlbCI+UFJPQ0VTU0lORzwvc3Bhbj48L2Rpdj48L2ZvcmVpZ25vYmplY3Q+PC9nPjwvZz48ZyBjbGFzcz0ibm9kZSBzdGF0ZWRpYWdyYW0tc3RhdGUiIGlkPSJzdGF0ZS1TVE9QUEVELTEwIiB0cmFuc2Zvcm09InRyYW5zbGF0ZSgyNTYuODIwMzEyNSwgNjA5LjUpIj48cmVjdCBjbGFzcz0iYmFzaWMgbGFiZWwtY29udGFpbmVyIiB4PSItNDUuNTg1OTM3NSIgeT0iLTE2LjUiIHdpZHRoPSI5MS4xNzE4NzUiIGhlaWdodD0iMzMiIC8+PGcgY2xhc3M9ImxhYmVsIiB0cmFuc2Zvcm09InRyYW5zbGF0ZSgtMzguMDg1OTM3NSwgLTkpIj48Zm9yZWlnbm9iamVjdCB3aWR0aD0iNzYuMTcxODc1IiBoZWlnaHQ9IjE4Ij48ZGl2IHhtbG5zPSJodHRwOi8vd3d3LnczLm9yZy8xOTk5L3hodG1sIiBzdHlsZT0iZGlzcGxheTppbmxpbmUtYmxvY2s7d2hpdGUtc3BhY2U6bm93cmFwIj48c3BhbiBjbGFzcz0ibm9kZUxhYmVsIj5TVE9QUEVEPC9zcGFuPjwvZGl2PjwvZm9yZWlnbm9iamVjdD48L2c+PC9nPjxnIGNsYXNzPSJub2RlIHN0YXRlZGlhZ3JhbS1zdGF0ZSIgaWQ9InN0YXRlLURPTkUtMTEiIHRyYW5zZm9ybT0idHJhbnNsYXRlKDM4LjYxNzE4NzUsIDYwOS41KSI+PHJlY3QgY2xhc3M9ImJhc2ljIGxhYmVsLWNvbnRhaW5lciIgeD0iLTMwLjYxNzE4NzUiIHk9Ii0xNi41IiB3aWR0aD0iNjEuMjM0Mzc1IiBoZWlnaHQ9IjMzIiAvPjxnIGNsYXNzPSJsYWJlbCIgdHJhbnNmb3JtPSJ0cmFuc2xhdGUoLTIzLjExNzE4NzUsIC05KSI+PGZvcmVpZ25vYmplY3Qgd2lkdGg9IjQ2LjIzNDM3NSIgaGVpZ2h0PSIxOCI+PGRpdiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMTk5OS94aHRtbCIgc3R5bGU9ImRpc3BsYXk6aW5saW5lLWJsb2NrO3doaXRlLXNwYWNlOm5vd3JhcCI+PHNwYW4gY2xhc3M9Im5vZGVMYWJlbCI+RE9ORTwvc3Bhbj48L2Rpdj48L2ZvcmVpZ25vYmplY3Q+PC9nPjwvZz48ZyBjbGFzcz0ibm9kZSBkZWZhdWx0IiBpZD0ic3RhdGUtcm9vdF9lbmQtMTIiIHRyYW5zZm9ybT0idHJhbnNsYXRlKDI2Ny45NzI2NTYyNSwgNjgzKSI+PGNpcmNsZSBjbGFzcz0ic3RhdGUtc3RhcnQiIHI9IjciIHdpZHRoPSIxNCIgaGVpZ2h0PSIxNCI+PC9jaXJjbGU+PGNpcmNsZSBjbGFzcz0ic3RhdGUtZW5kIiByPSI1IiB3aWR0aD0iMTAiIGhlaWdodD0iMTAiPjwvY2lyY2xlPjwvZz48L2c+PC9nPjwvZz48L3N2Zz4=)

The workflow starts when a user posts a new batch request. In this step the system:

- creates a new batch task with the status `CREATED`,
- validates the user's input (except the evalscript),
- ensures the user's account has at least 1000 PUs,
- uploads a JSON of the original request to the user's bucket,
- and returns the overview of the created task.

The user can then decide to either request an additional analysis of the task or start the processing. When an additional analysis is requested:

- the status of the task changes to `ANALYSING`,
- the evalscript is validated,
- a [feature manifest](../../APIs/SentinelHub/BatchV2.llms.md#feature-manifest) file is uploaded to the user's bucket,
- after the analysis is finished, the status of the task changes to `ANALYSIS_DONE`.

If the user chooses to directly start processing, the system still executes the analysis but when the analysis is done it automatically proceeds with processing. This is not explicitly shown in the diagram in order to keep it simple.

When the user starts the processing:

- the status of the task changes to `PROCESSING` (this may take a while, depending on the load on the service),
- the processing starts,
- an [execution database](../../APIs/SentinelHub/BatchV2.llms.md#execution-database) is periodically uploaded to the user's bucket,
- spent processing units are billed periodically.

When the processing is finished, the status of the task changes to `DONE`.

#### Stopping the request

A task might be stopped for the following reasons:

- it's requested by a user (user action),
- user is out of processing units,
- something is wrong with the processing of the task (e.g. the system is not able to process the data).

A user may stop the request in following states: `ANALYSING`, `ANALYSIS_DONE` and `PROCESSING`. However:

- if the status is `ANALYSING`, the analysis will complete,
- if the status is `PROCESSING`, all features (polygons) that have been processed or are being processed at that moment are charged for,
- user is not allowed to restart the task in the next 30 minutes.

------------------------------------------------------------------------

## Input features

BatchV2 API supports two ways of specifying the input features of your batch task:

1.  Pre-defined [Tiling Grid](../../APIs/SentinelHub/BatchV2.llms.md#1-tiling-grid)
2.  User-defined [GeoPackage](../../APIs/SentinelHub/BatchV2.llms.md#2-geopackage)

### 1. Tiling Grid

For more effective processing we divide the area of interest into tiles and process each tile separately. While `process` API uses grids which come together with each datasource for processing of the data, the `batch` API uses one of the predefined tiling grids. The tiling grids 0-2 are based on the [Sentinel-2 tiling](https://sentinel.esa.int/web/sentinel/missions/sentinel-2/data-products) in WGS84/UTM projection with some adjustments:

- The width and height of tiles in the original Sentinel 2 grid is 100 km while the width and height of tiles in our grids are given in the table below.
- All redundant tiles (i.e. fully overlapped tiles) are removed.

All available tiling grids can be requested with (*NOTE: To run this example you need to first create an OAuth client as is explained [here](../../APIs/SentinelHub/Overview/Authentication.llms.md#python)*):

``` python
url = "https://sh.dataspace.copernicus.eu/batch/v2/tilinggrids/"

response = oauth.request("GET", url)

response.json()
```

This will return the list of available grids and information about tile size and available resolutions for each grid. Currently, available grids are:

| name | id | tile size | resolutions | coverage | output CRS | download the grid \[zip with shp file\] \*\* |
|:---|:---|:---|:---|:---|:---|:---|
| UTM 20km grid | 0 | 20040 m | 10 m, 20 m, 30m\*, 60 m | World, latitudes from -80.7° to 80.7° | UTM | [UTM 20km grid](https://s3.eu-central-1.amazonaws.com/sh-batch-grids/tiling-grid-0.zip) |
| UTM 10km grid | 1 | 10000 m | 10 m, 20 m | World, latitudes from -80.6° to 80.6° | UTM | [UTM 10km grid](https://s3.eu-central-1.amazonaws.com/sh-batch-grids/tiling-grid-1.zip) |
| UTM 100km grid | 2 | 100080 m | 30m\*, 60 m, 120 m, 240 m, 360 m | World, latitudes from -81° to 81° | UTM | [UTM 100km grid](https://s3.eu-central-1.amazonaws.com/sh-batch-grids/tiling-grid-2.zip) |
| WGS84 1 degree grid | 3 | 1 ° | 0.0001°, 0.0002° | World, all latitudes | WGS84 | [WGS84 1 degree grid](https://s3.eu-central-1.amazonaws.com/sh-batch-grids/tiling-grid-3.zip) |
| LAEA 100km grid | 6 | 100000 m | 40 m, 50 m, 100 m | Europe, including Turkey, Iceland, Svalbald, Azores, and Canary Islands | EPSG:3035 | [LAEA 100km grid](https://s3.eu-central-1.amazonaws.com/sh-batch-grids/tiling-grid-6.zip) |
| LAEA 20km grid | 7 | 20000 m | 10 m, 20 m | Europe, including Turkey, Iceland, Svalbald, Azores, and Canary Islands | EPSG:3035 | [LAEA 20km grid](https://s3.eu-central-1.amazonaws.com/sh-batch-grids/tiling-grid-7.zip) |

\*\* The geometries of the tiles are reprojected to WGS84 for download. Because of this and other reasons the geometries of the output rasters may differ from the tile geometries provided here.

To use `20km` grid with 60 m resolution, for example, specify `id` and `resolution` parameters of the `tilingGrid` object when creating a new batch request (see an example of [full request](../../APIs/SentinelHub/BatchV2/Examples.llms.md#create-a-batchv2-processing-request)) as:

``` json
{
  ...
  "input": {
    "type" : "tiling-grid",
    "id": 0,
    "resolution": 60.0
  },
  ...
}
```

### 2. GeoPackage

In addition to the tiling grids, BatchV2 API now also support user-defined features through [GeoPackages](https://www.geopackage.org/spec/). This allows you to specify features of any shape as long as the underlying geometry is a POLYGON or MULTIPOLYGON in an **EPSG compliant** CRS listed [here](../../APIs/SentinelHub/Process/Crs.llms.md). The GeoPackage can also have multiple layers, offering more flexibility in specifying features in multiple CRS.

The GeoPackage must adhere to the [GeoPackage spec](https://www.geopackage.org/spec/) and contain at **least one feature table with any name**. The table must include a column that holds the geometry data. This column can be named arbitrarily, but it must be listed as the geometry column in the `gpkg_geometry_columns` table. The table schema should include the following columns:

| Column | Type | Example |
|:---|:---|:---|
| id - primary key | INTEGER **(UNIQUE)** | 1000 |
| identifier | TEXT **(UNIQUE)** | FEATURE_NAME |
| geometry | POLYGON or MULTIPOLYGON | Feature geometry representation in GeoPackage WKB format |
| width | INTEGER | 1000 |
| height | INTEGER | 1000 |
| resolution | REAL | 0.005 |

#### Caveats

- You must specify either both width and height, or alternatively, specify resolution. If both values are provided, width and height will be used, and resolution will be ignored.
- The feature table must use a CRS that is **EPSG compliant**.
- `identifier` values must not be null and unique across all feature tables.
- There can be a maximum of 700.000 features in the GeoPackage.
- The feature output width and height cannot exceed 3500 by 3500 pixels or the equivalent in resolution.

Below you will find a list of example GeoPackages that serve as a showcase of how a GeoPackage file should be structured. Please note that these examples do not serve as production-ready GeoPackages and should only be used for testing purposes. If you'd like to use these tiling grids for processing, use the equivalent tiling grid with the tiling grid input instead.

| name | id | output CRS | geopackage |
|:---|:---|:---|:---|
| UTM 20km grid | 0 | UTM | [UTM 20km grid](https://s3.eu-central-1.amazonaws.com/sh-batch-grids/tiling-grid-0.gpkg) |
| UTM 10km grid | 1 | UTM | [UTM 10km grid](https://s3.eu-central-1.amazonaws.com/sh-batch-grids/tiling-grid-1.gpkg) |
| UTM 100km grid | 2 | UTM | [UTM 100km grid](https://s3.eu-central-1.amazonaws.com/sh-batch-grids/tiling-grid-2.gpkg) |
| WGS84 1 degree grid | 3 | WGS84 | [WGS84 1 degree grid](https://s3.eu-central-1.amazonaws.com/sh-batch-grids/tiling-grid-3.gpkg) |
| LAEA 100km grid | 6 | EPSG:3035 | [LAEA 100km grid](https://s3.eu-central-1.amazonaws.com/sh-batch-grids/tiling-grid-6.gpkg) |
| LAEA 20km grid | 7 | EPSG:3035 | [LAEA 20km grid](https://s3.eu-central-1.amazonaws.com/sh-batch-grids/tiling-grid-7.gpkg) |

An example of a batch task with GeoPackage input is available [here](../../APIs/SentinelHub/BatchV2/Examples.llms.md#option-3-geopackage-input-and-geotiff-output).

### Area of Interest and PUs

When using either [Tiling Grid](../../APIs/SentinelHub/BatchV2.llms.md#1-tiling-grid) or [GeoPackage](../../APIs/SentinelHub/BatchV2.llms.md#2-geopackage) as input, the features that end up being processed are determined by the `processRequest.input.bounds` parameter specified in the request, called Area of Interest or AOI.

The way the AOI parameter is used and its effect depend on the input type used:

- Tiling grid: The AOI **must** be specified in the request. Only the tiles (features) that intersect with the AOI will be processed.
- GeoPackage: The AOI can optionally be omitted. If the AOI is omitted, all the features inside your GeoPackage will be processed. Conversely, if AOI is specified, only the features that intersect with the AOI will be processed.

Please note that in both cases of input types, if the feature is only **partially** covered by the AOI, the feature will be processed in its **entirety**.

You are only charged PUs for the features that are processed. If a feature does not intersect with the AOI, it will not be charged for.

------------------------------------------------------------------------

## Processing results

The outputs of a batch task will be stored to your object storage in either:

1.  GeoTIFF (and JSON for metadata) or
2.  Zarr format

### 1. GeoTIFF output format

**The GeoTIFF format will be used if your request includes the `output.type` parameter set to `raster`, along with other relevant parameters specified in the [BatchV2 API reference](../../APIs/SentinelHub/ApiReference.llms.md#tag/batch_v2_process/operation/createNewBatchV2ProcessingRequest). An example of a batch task with GeoTIFF output is available [here](../../APIs/SentinelHub/BatchV2/Examples.llms.md#option-1-geotiff-format-output).**

By default, the results will be organized in sub-folders where one sub-folder will be created for each feature. Each sub-folder might contain one or more images depending on how many outputs were defined in the [evalscript](../../APIs/SentinelHub/Evalscript/Functions.llms.md#setup-function) of the request. For example:

You can also customize the sub-folder structure and file naming as described in the `delivery` parameter under `output` in [BatchV2 API reference](../../APIs/SentinelHub/ApiReference.llms.md#tag/batch_v2_process/operation/createNewBatchV2ProcessingRequest).

You can choose to return your GeoTIFF files as Cloud Optimized GeoTIFF (COG), by setting the `cogOutput` parameter under `output` in your request as `true`. Several advanced COG options can be selected as well - read about the parameter in [BatchV2 API reference](../../APIs/SentinelHub/ApiReference.llms.md#tag/batch_v2_process/operation/createNewBatchV2ProcessingRequest).

The output projection depends on the selected input, either tiling grid or GeoPackage:

1.  If the input is a tiling grid, the results of batch processing will be in the projection of the selected [tiling grid](../../APIs/SentinelHub/BatchV2.llms.md#1-tiling-grid). For UTM-based grids, each part of the AOI (area of interest) is delivered in the UTM zone with which it intersects. In other words, in case your AOI intersects with more UTM zones, the results will be delivered as tiles in different UTM zones (and thus different CRSs).
2.  If the input is a GeoPackage, the results will be in the same CRS as the input feature's CRS.

### 2. Zarr output format

The Zarr format will be used if your request includes the `output.type` parameter set to `zarr`, along with other relevant parameters specified in the [BatchV2 API reference](../../APIs/SentinelHub/ApiReference.llms.md#tag/batch_v2_process/operation/createNewBatchV2ProcessingRequest). An example of a batch request with Zarr output is available [here](../../APIs/SentinelHub/BatchV2/Examples.llms.md#option-2-zarr-format-output). Your request **must** only have one band per output and the `application/json` format in responses is **not** supported.

The outputs of batch processing will be stored as a single Zarr group containing one data array for each evalscript output and multiple coordinate arrays. The output will be stored in a subfolder named after the `requestId` that you pass to the API in the `delivery.s3.url` parameter under `output`.

------------------------------------------------------------------------

## Ingesting results into BYOC

#### Purpose

Enables automatic ingestion of processing results into a BYOC collection, allowing you to:

- Access data with Processing API, by using the collection ID
- Create a configuration with custom layers
- Make OGC requests to a configuration
- View data in EO Browser

In order to enable this functionality, user needs to specify either id of an existing BYOC collection (`collectionId`) or set `createCollection = true`.

``` json
{
  ...
  "output": {
    ...
    "createCollection": true,
    "collectionId": "<byoc-collection-id>",
    ...
  },
  ...
}
```

If collectionId is provided, the existing collection will be used for data ingestion.

If `createCollection` is set to `true` and `collectionId` is not provided, a new BYOC collection will be created automatically and the collection bands will be set according to the request output `responses` definitions.

Regardless of whether the user specifies an existing collection or requests a new one, processed data will still be uploaded to the users bucket, where they will be available for download and analysis.

When creating a new batch collection, one has to be careful to:

- Make sure that `cogOutput=true` and that the output format is a `image/tiff`
- If an existing BYOC collection is used, make sure that `identifier` and `sampleType` from the output definition(s) match the name and the type of the BYOC band(s). Single band and multi-band outputs are supported.
- If multi-band output is used in the request, the additionally generated bands will be named using a numerical suffix in ascending order (e.g. 2, ... 99). For example, if the `output: { id: "result", bands: 3 }` is used in the evalscript setup function, the produced BYOC bands will be named: `result` for band 1, `result2` for band 2 and `result3` for band 3. Make sure that no other output band has any of these automatically generated names, as this will throw an error during the analysis phase. The `output: [{ id: "result", bands: 3 },{ id: "result2", bands: 1 }]` will throw an exception.
- Keep sampleType in mind, as the values the evalscript returns when creating a collection will be the values available when making a request to access it.

#### Mandatory bucket settings

Regardless of the credentials provided in the request, you still need to set a bucket policy to allow Sentinel Hub services to access the data. For detailed instructions on how to configure your bucket policy, please refer to the [BYOC bucket settings documentation](../../APIs/SentinelHub/Byoc.llms.md#aws-bucket-settings).

## Feature Manifest

#### Purpose

- Provides a detailed overview of features scheduled for processing during the `PROCESSING` step.
- Enables users to verify feature information and corresponding output paths prior to processing.

#### Key Information

- **File Type:** [GeoPackage](https://www.geopackage.org/spec/)
- **File Name:** `featureManifest-<requestId>.gpkg`
- **Location:** Root folder of the specified output delivery path
- **Structure:**
  - May contain multiple feature tables, one per distinct CRS used by the features.
  - Table names follow the format `feature_<crs-id>` (e.g. `feature_4326`).

During task analysis, the system will upload a file to the user's bucket called the `featureManifest-<requestId>.gpkg`. This file is a GeoPackage that contains basic information about the features that will be processed during the `PROCESSING` step. It is intended to be used by users to check the features that will be processed and their corresponding output paths.

If the output type is set to `raster`, the output paths will be the paths to the GeoTIFF files. If the output type is `zarr`, the output paths will just be the root of the output folder.

The database may contain multiple feature tables, one feature table for each CRS of all features. The tables will be named `feature_<crs-id>`, e.g. `feature_4326`.  
The schema of feature tables inside the database is currently the following:

| Name | Type | Description |
|:---|:---|:---|
| fid | INTEGER | Auto-incrementing ID |
| outputId | TEXT | Output identifier defined in the `processRequest` |
| identifier | TEXT | ID of the feature |
| path | TEXT | The object storage path URI where the output of this feature will be uploaded to |
| width | INTEGER | Width of the feature in pixels |
| height | INTEGER | Height of the feature in pixels |
| geometry | GEOMETRY | Feature geometry representation in GeoPackage WKB format |

------------------------------------------------------------------------

## Execution database

### Purpose

The Execution Database serves as a monitoring tool for tracking the progress of feature execution within a specific task. It provides users with insight into the status of each feature being processed.

### Key Information

- **File Type:** SQLite
- **File Name:** `execution-<requestId>.sqlite`
- **Location:** Root folder of specified output delivery path
- **Structure:**
  - Contains a single table called `features`.

You can monitor the execution of your features for a specific task by checking the SQLite database that is uploaded to your bucket. The database contains the name and status of each feature. The database is updated periodically during the execution of the task.

The database can be found in your bucket in the root output folder and is named `execution-<requestId>.sqlite`.

The schema of the `features` table is currently the following:

| Name | Type | Description |
|:---|:---|:---|
| id | INTEGER | Numerical ID of the feature |
| name | TEXT | Textual ID of the feature |
| status | TEXT | Status of the feature |
| error | TEXT | Error message in case processing has failed |
| delivered | BOOLEAN | `True` if output delivered to delivery bucket, otherwise `False` |

The status of the feature can be one of the following:

- **PENDING**: The feature is waiting to be processed.
- **DONE**: Feature was successfully processed.  
  Caveat: If there was no data to process for this feature, the feature will still be marked with status `DONE` but with a '**No data**' message in the error column.
- **FATAL**: Feature has failed X amount of times and will not be retried. The error column details the issue.

------------------------------------------------------------------------

## Bucket settings and access

The results will be delivered in your own bucket hosted at Copernicus Data Space Ecosystem. To access your bucket accessKey and secretAccessKey pair have to bo provided in your request.

``` default
s3 = {
    "url": "s3://<your-bucket>/<path>",
    "accessKey": "<your-bucket-access-key>",
    "secretAccessKey": "<your-bucket-secret-access-key>"
}
```

If you do not yet have a bucket at Copernicus Data Space Ecosystem, please follow [these steps](https://creodias.docs.cloudferro.com/en/latest/s3/Create-S3-bucket-and-use-it-in-Sentinel-Hub-requests.html) to get one.

### Bucket regions

Supported regions are **WAW3-1**, **WAW3-2** and **WAW4-1**.

## Examples

[Example of Batch Processing Workflow](../../APIs/SentinelHub/BatchV2/Examples.llms.md)
