import tkinter as tk
from tkinter import ttk, messagebox
import platform
import subprocess
import sys
import os

class SerialNumberApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Número de Série do Sistema")
        
        # Configurar o tema e estilo
        style = ttk.Style()
        style.theme_use('clam')  # Usar um tema moderno
        
        # Configurar a janela
        self.root.geometry("600x400")
        self.root.resizable(True, True)
        
        # Criar o frame principal
        main_frame = ttk.Frame(root, padding="20")
        main_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        self.root.columnconfigure(0, weight=1)
        self.root.rowconfigure(0, weight=1)
        
        # Título
        title_label = ttk.Label(
            main_frame,
            text="Informações do Sistema",
            font=('Helvetica', 16, 'bold')
        )
        title_label.grid(row=0, column=0, columnspan=2, pady=(0, 20))
        
        # Frame para informações
        info_frame = ttk.LabelFrame(main_frame, text="Detalhes", padding="10")
        info_frame.grid(row=1, column=0, columnspan=2, sticky=(tk.W, tk.E, tk.N, tk.S))
        main_frame.columnconfigure(0, weight=1)
        
        # Área de texto para exibir as informações
        self.info_text = tk.Text(info_frame, height=10, width=50, wrap=tk.WORD)
        self.info_text.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        
        # Scrollbar para a área de texto
        scrollbar = ttk.Scrollbar(info_frame, orient=tk.VERTICAL, command=self.info_text.yview)
        scrollbar.grid(row=0, column=1, sticky=(tk.N, tk.S))
        self.info_text['yscrollcommand'] = scrollbar.set
        
        info_frame.columnconfigure(0, weight=1)
        info_frame.rowconfigure(0, weight=1)
        
        # Botões
        button_frame = ttk.Frame(main_frame)
        button_frame.grid(row=2, column=0, columnspan=2, pady=20)
        
        ttk.Button(
            button_frame,
            text="Copiar",
            command=self.copy_to_clipboard
        ).grid(row=0, column=0, padx=5)
        
        ttk.Button(
            button_frame,
            text="Fechar",
            command=self.root.destroy
        ).grid(row=0, column=1, padx=5)
        
        # Carregar informações iniciais
        self.get_system_info()
    
    def get_serial_number(self):
        system = platform.system().lower()
        
        try:
            if system == 'windows':
                # Windows - usando wmic
                cmd = 'wmic bios get serialnumber'
                output = subprocess.check_output(cmd, shell=True).decode()
                serial = output.split('\n')[1].strip()
            
            elif system == 'darwin':
                # macOS - usando system_profiler
                cmd = 'system_profiler SPHardwareDataType | grep "Serial Number"'
                output = subprocess.check_output(cmd, shell=True).decode()
                serial = output.split(': ')[1].strip()
            
            elif system == 'linux':
                # Linux - verificando diferentes locais
                possible_files = [
                    '/sys/devices/virtual/dmi/id/product_serial',
                    '/sys/firmware/dmi/tables/smbios_type_1'
                ]
                
                serial = "Não encontrado"
                for file in possible_files:
                    if os.path.exists(file):
                        try:
                            with open(file, 'r') as f:
                                serial = f.read().strip()
                            if serial and serial != "To be filled by O.E.M.":
                                break
                        except:
                            continue
                
                # Se não encontrou nos arquivos, tenta dmidecode
                if serial == "Não encontrado":
                    try:
                        cmd = 'sudo dmidecode -s system-serial-number'
                        serial = subprocess.check_output(
                            cmd, shell=True, stderr=subprocess.DEVNULL
                        ).decode().strip()
                    except:
                        pass
            
            else:
                serial = "Sistema operacional não suportado"
            
            return serial if serial and serial != "To be filled by O.E.M." else "Não disponível"
        
        except Exception as e:
            return f"Erro ao obter número de série: {str(e)}"
    
    def get_system_info(self):
        self.info_text.delete(1.0, tk.END)
        
        # Coletar informações
        info = [
            ("Sistema Operacional", platform.system()),
            ("Versão do SO", platform.version()),
            ("Arquitetura", platform.machine()),
            ("Processador", platform.processor()),
            ("Número de Série", self.get_serial_number()),
            ("Nome do Computador", platform.node())
        ]
        
        # Adicionar informações ao texto
        max_label_length = max(len(label) for label, _ in info)
        for label, value in info:
            padded_label = label.ljust(max_label_length)
            self.info_text.insert(tk.END, f"{padded_label}: {value}\n")
        
        self.info_text.configure(state='normal')
    
    def copy_to_clipboard(self):
        info = self.info_text.get(1.0, tk.END).strip()
        self.root.clipboard_clear()
        self.root.clipboard_append(info)
        messagebox.showinfo(
            "Copiado",
            "Informações copiadas para a área de transferência!"
        )

def main():
    root = tk.Tk()
    app = SerialNumberApp(root)
    root.mainloop()

if __name__ == '__main__':
    main()