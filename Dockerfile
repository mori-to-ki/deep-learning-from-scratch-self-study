# ベースイメージ
FROM python:3.10-slim

# 必要なシステム依存パッケージのインストールと
# NumPy／Matplotlib の導入
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
      build-essential \
      libfreetype6-dev \
      libpng-dev && \
    pip install --upgrade pip && \
    pip install --no-cache-dir \
      numpy \
      matplotlib \
      Image && \
    apt-get purge -y --auto-remove build-essential && \
    rm -rf /var/lib/apt/lists/*

# 作業ディレクトリを設定
WORKDIR /app

# python実行ディレクトリを指定
ENV PYTHONPATH=$PYTHONPATH:/app

# ホスト側の全ファイルをコンテナ内にコピー
COPY . /app

# デフォルトコマンド
CMD ["python3"]
