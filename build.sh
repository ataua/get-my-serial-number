#!/bin/bash

# Criar ambiente virtual para isolar as dependências
python3 -m venv venv

# Ativar o ambiente virtual
source venv/bin/activate

# Instalar PyInstaller
pip install pyinstaller

# Gerar executável para Linux
pyinstaller --clean --onefile --windowed \
    --name "serial-number-app-linux" \
    --add-data "README.md:." \
    serial_number_app.py

# Criar pasta para os executáveis
mkdir -p dist/releases

# Mover executável Linux para pasta releases
mv dist/serial-number-app-linux dist/releases/

# Limpar arquivos temporários
rm -rf build/
rm -rf *.spec

# Criar arquivo README para a pasta releases
cat > dist/releases/README.txt << EOL
Aplicativo para Visualização do Número de Série

Instruções:

Linux:
1. Abra um terminal na pasta do executável
2. Torne o arquivo executável: chmod +x serial-number-app-linux
3. Execute: ./serial-number-app-linux
Nota: Pode ser necessário executar com sudo para acessar algumas informações

Windows:
1. Duplo clique em serial-number-app-windows.exe
Nota: Pode ser necessário executar como administrador

macOS:
1. Duplo clique em serial-number-app-mac
2. Se necessário, use: chmod +x serial-number-app-mac no terminal
EOL

echo "Executável para Linux foi gerado em dist/releases/"
echo "Nota: Para gerar executáveis para Windows e macOS, execute este script no sistema operacional correspondente"