# docker-go

Docker で Go アプリケーションを開発・実行するためのスタータープロジェクトです。

- [setup](#setup)
- [docker commands](#docker-commands)
- [start](#start)
- [containers](#containers)
- [project-structure](#project-structure)

### setup
```bash
cp .env.template .env
```
必要に応じてポート番号や DB 接続情報などを調整してください。

### docker commands
```bash
# build & up container
docker compose up -d --build
$ make up
# destroy
docker compose down --rmi all --volumes --remove-orphans
$ make destroy
# attach to go container (docker compose exec go bash)
$ make go
# down container
docker compose down
$ make down
```

### start
1. run container
```bash
$ make up
```
2. check http server (default port: 8080)
```bash
$ curl http://localhost:8080
$ curl http://localhost:8080/healthz
```

### containers
- go
  - Go アプリケーション実行用のコンテナ
- mysql
  - デフォルトで起動する MySQL データベースコンテナ
- postgres (コメントアウト)
  - 必要に応じて有効化できる PostgreSQL データベースコンテナ

#### switch to PostgreSQL
`docker-compose.yml` の `postgres` サービスをコメント解除し、`mysql` サービスをコメントアウトまたは削除してください。`go` サービスの `depends_on` も合わせて更新し、`.env` の PostgreSQL 変数も必要に応じて編集します。

### project-structure
```
/project_root
├── infra/docker/go/      # Go 用 Dockerfile
├── src/                  # Go アプリケーションのソースコード
│   ├── cmd/server/main.go
│   └── go.mod
├── docker-compose.yml       # アプリケーション & DB 用コンテナ定義
├── Makefile
└── README.md (this file)
```
