import tkinter as tk; from tkinter import ttk; from datetime import datetime
class SistemadeTutorias:  
    def __init__(self, root):
        self.root = root; self.root.title("Registro de Tutorias"); self.registros = []  
        ttk.Label(root, text="Asignatura:").grid(row=0, column=0); self.asignatura = ttk.Combobox(root, values=["Sistemas de Informacion", "Aplicaciones Moviles", "Electiva II", "Desarrollo de Entorno Web", "Servicios Telematicos", "Seguridad Informatica"]); self.asignatura.grid(row=0, column=1)
        ttk.Label(root, text="ID Estudiante:").grid(row=1, column=0); self.id_est = ttk.Entry(root); self.id_est.grid(row=1, column=1)
        ttk.Button(root, text="Registrar", command=self.registrar).grid(row=2, columnspan=2); self.tree = ttk.Treeview(root, columns=("Fecha", "Asignatura", "ID"), show="headings", height=8); self.tree.heading("Fecha", text="Fecha"); self.tree.heading("Asignatura", text="Asignatura"); self.tree.heading("ID", text="ID Estudiante"); self.tree.column("Fecha", width=120); self.tree.column("Asignatura", width=150); self.tree.column("ID", width=100); self.tree.grid(row=3, columnspan=2)
    def registrar(self):  
        registro = (datetime.now().strftime("%d/%m %H:%M"), self.asignatura.get(), self.id_est.get());  self.registros.append(registro); self.tree.insert("", "end", values=registro); self.id_est.delete(0, "end")
if __name__ == "__main__": root = tk.Tk(); SistemadeTutorias(root); root.mainloop()
