# PolyDock 🐳

**PolyDock (Polyglot + Docker)** is a unified Docker-based development environment that brings together multiple language stacks and frameworks into a single repository — with full commit history preserved for each.

This project was born out of a need to manage multiple dev containers more efficiently, and to provide a centralized, reusable environment for full-stack development.

---

## 📦 Included Environments

Each environment is contained in its own directory:

```
docker-python/      # Python dev environment
docker-react/       # React dev environment
docker-java/        # Java dev environment
docker-html-css/    # HTML & CSS boilerplate
docker-node/        # Node.js environment
docker-laravel/     # Laravel (PHP) environment
docker-jupyter/     # Jupyter Notebook environment
```

---

## 🚀 Usage

Each environment is self-contained and can be launched individually.

Example (Python):

```bash
cd docker-python
docker build -t polydock-python .
docker run --rm -it polydock-python
```

You can also integrate environments into a unified `docker-compose.yml` or `Makefile` (coming soon!).

---

## 📚 Background

This project is a result of consolidating scattered Docker repositories into one place with full history.  
Read the full story on Qiita 👉  
📝 [リポジトリの棚卸し：複数のDocker環境を履歴付きで1つに統合した話](https://qiita.com/your-link-here)

---

## 🧭 Roadmap

- [ ] Add unified `Makefile` for quick access
- [ ] Compose file to spin up multiple environments
- [ ] Add test cases and CI
- [ ] Optional: GitHub Pages for project docs

---

## 🛠️ Requirements

- Docker
- (Optional) Docker Compose
- git-filter-repo (if doing similar repo work)

---

## 🐳 Author

Created with love by [@hellomyzn](https://github.com/hellomyzn)
