import tkinter as tk
from tkinter import filedialog
from moviepy.editor import *

def import_file():
    file_path = filedialog.askopenfilename()
    return file_path

def export_file(file, format, resolution, framerate):
    file_name = file.split("/")[-1].split(".")[0] + "." + format
    output_path = filedialog.asksaveasfilename(defaultextension="."+format, initialfile=file_name)
    clip = VideoFileClip(file)
    clip_resized = clip.resize(resolution)
    clip_resized.write_videofile(output_path, codec='libx264', fps=framerate)

def main():
    root = tk.Tk()
    root.title("CJK Video Converter")
    
    root.columnconfigure(0, weight=1)
    root.columnconfigure(1, weight=1)
    root.columnconfigure(2, weight=1)
    root.rowconfigure(0, weight=1)
    root.rowconfigure(1, weight=1)
    root.rowconfigure(2, weight=1)
    root.rowconfigure(3, weight=1)
    root.rowconfigure(4, weight=1)

    style = {'font': ('Arial', 12), 'padx': 5, 'pady': 5}

    file_path = tk.StringVar()

    def on_import_click():
        file_path.set(import_file())

    def on_export_click():
        format = format_var.get()
        resolution = (int(width_entry.get()), int(height_entry.get()))
        framerate = int(fps_entry.get())
        export_file(file_path.get(), format, resolution, framerate)

    import_button = tk.Button(root, text="Import File", command=on_import_click, **style)
    import_button.grid(row=0, column=0, columnspan=3, sticky='ew')

    format_var = tk.StringVar()
    format_var.set("mp4")
    format_label = tk.Label(root, text="Choose Format:", **style)
    format_label.grid(row=1, column=0)
    format_option = tk.OptionMenu(root, format_var, "avi", "mp4", "mov")
    format_option.grid(row=1, column=1, columnspan=2, sticky='ew')

    resolution_label = tk.Label(root, text="Set Resolution (Width x Height in px):", **style)
    resolution_label.grid(row=2, column=0)
    width_entry = tk.Entry(root)
    width_entry.grid(row=2, column=1, sticky='ew')
    height_entry = tk.Entry(root)
    height_entry.grid(row=2, column=2, sticky='ew')

    fps_label = tk.Label(root, text="Set Frame Rate (FPS):", **style)
    fps_label.grid(row=3, column=0)
    fps_entry = tk.Entry(root)
    fps_entry.grid(row=3, column=1, columnspan=2, sticky='ew')

    export_button = tk.Button(root, text="Export File", command=on_export_click, **style)
    export_button.grid(row=4, column=0, columnspan=2, sticky='ew')

    exit_button = tk.Button(root, text="Exit Program", command=root.quit, **style)
    exit_button.grid(row=4, column=2, sticky='ew')

    root.mainloop()

if __name__ == "__main__":
    main()
  