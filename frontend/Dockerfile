# 最新のBunの公式イメージを使用
FROM oven/bun:latest

# 作業ディレクトリを設定
WORKDIR /app

# パッケージリストをコピー
COPY package.json ./

# 依存関係のインストール（キャッシュを利用せず最新にするため）
RUN bun install --no-cache

# ソースコードをコピー（必要なファイルだけコピー）
COPY . .

# 開発サーバーを起動
CMD ["bun", "dev"]
