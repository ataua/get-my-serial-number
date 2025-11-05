# Get Serial Number App

Um aplicativo desktop simples para obter o número de série e outras informações do sistema.

## Funcionalidades

- Exibe o número de série do sistema
- Mostra informações adicionais do sistema operacional
- Interface gráfica amigável
- Botão para copiar todas as informações
- Suporte para Windows, Linux e macOS

## Requisitos

- Python 3.6 ou superior
- tkinter (geralmente já vem instalado com Python)

## Como usar

### Usuários finais

1. Baixe o executável correspondente ao seu sistema operacional
2. Execute o arquivo baixado
3. O aplicativo mostrará as informações do sistema
4. Use o botão "Copiar" para copiar todas as informações

### Desenvolvedores

1. Clone este repositório
2. Certifique-se de que tem Python 3.6+ instalado
3. Execute o aplicativo:
   ```bash
   python serial_number_app.py
   ```

## Notas importantes

### Windows
- O número de série é obtido através do comando `wmic`
- Pode ser necessário executar como administrador em alguns casos

### Linux
- O número de série é obtido de `/sys/devices/virtual/dmi/id/product_serial`
- Alternativamente, usa `dmidecode` (pode requerer sudo)
- Em alguns sistemas, pode ser necessário executar com privilégios de administrador

### macOS
- O número de série é obtido através do `system_profiler`
- Não requer privilégios especiais na maioria dos casos

## Observações

- Em alguns sistemas, o número de série pode não estar disponível ou pode retornar valores genéricos
- Alguns fabricantes podem usar valores padrão como "To be filled by O.E.M."
- O acesso a certas informações pode requerer privilégios de administrador