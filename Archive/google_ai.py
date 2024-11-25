import google.generativeai as genai
import tkinter as tk

def ai_query(prompt):
    genai.configure(api_key='AIzaSyCH6-EoKU7c2LaijhzKMRFTjQhh-NzeV1o')
    model = genai.GenerativeModel('gemini-pro')
    response = model.generate_content(prompt)
    return response.text


def main():

    def run_gemini():
        prompt = prompt_entry.get()
        genai.configure(api_key='AIzaSyCH6-EoKU7c2LaijhzKMRFTjQhh-NzeV1o')
        model = genai.GenerativeModel('gemini-pro')
        response = model.generate_content(prompt)
        response_text.delete(1.0, tk.END)
        response_text.insert(tk.END, response.text)

    root = tk.Tk()
    root.title("AI Interaction Tool")

    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    
    window_width = int(screen_width*0.5)
    window_height = int(screen_height*0.5)
    x = (screen_width - window_width) // 2
    y = (screen_height - window_height) // 2
    
    root.geometry(f"{window_width}x{window_height}+{x}+{y}")
    
    prompt_label = tk.Label(root, text="Enter your prompt for Gemini:")
    prompt_label.pack(pady=1)
    
    prompt_entry = tk.Entry(root)
    prompt_entry.pack(pady=5, fill = tk.X, expand=True)

    gemini_button = tk.Button(root, text="Commit", command=run_gemini)
    gemini_button.pack(pady=5)
    
    response_text = tk.Text(root, wrap=tk.WORD)
    response_text.pack(pady=5, fill = tk.BOTH, expand=True)
    
    root.mainloop()

main()

    # root = tk.Tk()
    # root.title("AI Interaction Tool")

    # screen_width = root.winfo_screenwidth()
    # screen_height = root.winfo_screenheight()

    # window_width = 300
    # window_height = 200
    # x = (screen_width - window_width) // 2
    # y = (screen_height - window_height) // 2

    # root.geometry(f"{window_width}x{window_height}+{x}+{y}")

