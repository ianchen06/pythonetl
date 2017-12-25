# Python ETL Jupyter Notebooks

## 如何安裝環境

以下是如何在Linux/Mac底下安裝Python環境

參照 https://github.com/pyenv/pyenv/wiki

### Linux

```
# 更新系統套件版本列表
sudo apt-get update

# 安裝C語言build tools
apt-get install -y make build-essential libssl-dev zlib1g-dev libbz2-dev libreadline-dev libsqlite3-dev wget curl llvm libncurses5-dev xz-utils tk-dev
```

### MacOS

```
# 安裝homebrew
/usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"

# 安裝一些系統套件
brew install openssl readline xz
```

### Linux/MacOS

```
# 安裝pyenv
curl -L https://raw.githubusercontent.com/pyenv/pyenv-installer/master/bin/pyenv-installer | bash
```