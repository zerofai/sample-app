# This is a namegen app that need to connect to a mariadb DB, the name of the table is names, and the DB info is retrieve via env var

To run without build
```
export dbHost=
export username=
export password=
go run main.go
```

To build the go on M1 for x64
```
go mod tidy         
go mod init main.go
GOOS=linux GOARCH=amd64 go build -o name_amd64
```