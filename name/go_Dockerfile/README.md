# This is the same as the python version, but in go lang

To run without build
```
go run main.go
```

To build the go on M1 for x64
```
go mod tidy         
go mod init main.go
GOOS=linux GOARCH=amd64 go build -o weather_amd64
```