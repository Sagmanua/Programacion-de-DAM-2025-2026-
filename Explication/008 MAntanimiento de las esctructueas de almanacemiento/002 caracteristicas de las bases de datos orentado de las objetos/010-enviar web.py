import json
import urllib.request
import urllib.error
import re

# Use the URL from your Cloudflare tunnel
OLLAMA_URL = "https://alert-make-teeth-reflections.trycloudflare.com/api/generate"
# We use llama3:latest since your server confirmed it is installed
MODEL = "llama3:latest"

def clean_html(raw_html):
    """Removes scripts, styles, and tags to help the AI see the data."""
    # Remove script and style blocks
    clean = re.sub(r'<(script|style).*?>.*?</\1>', '', raw_html, flags=re.DOTALL | re.IGNORECASE)
    # Remove all other HTML tags
    clean = re.sub(r'<.*?>', ' ', clean)
    # Clean up whitespace
    return ' '.join(clean.split())

def run_analysis():
    print(f"--- Starting Analysis using {MODEL} ---")
    
    try:
        # 1. Read the file
        with open("guardado.html", "r", encoding="utf-8") as f:
            raw_content = f.read()
        
        # 2. Pre-process the content
        text_content = clean_html(raw_content)
        
        # 3. Prepare the prompt
        prompt = (
            "Analyze the following text extracted from an HTML file. "
            "How many houses are listed or mentioned in this data? "
            f"\n\nDATA:\n{text_content}"
        )

        data = {
            "model": MODEL,
            "prompt": prompt,
            "stream": False
        }

        # 4. Send the request
        jsondata = json.dumps(data).encode("utf-8")
        req = urllib.request.Request(OLLAMA_URL, data=jsondata)
        req.add_header("Content-Type", "application/json")

        print("Sending data to Colab... (this might take a few seconds)")
        with urllib.request.urlopen(req) as response:
            res_body = response.read().decode("utf-8")
            result = json.loads(res_body)
            
            print("\n================ AI ANSWER ================")
            print(result.get("response"))
            print("===========================================")

    except FileNotFoundError:
        print("Error: 'guardado.html' not found. Make sure the file is in this folder.")
    except urllib.error.HTTPError as e:
        print(f"API Error {e.code}: {e.reason}")
        print("Detail:", e.read().decode())
    except Exception as e:
        print(f"Unexpected error: {e}")

if __name__ == "__main__":
    run_analysis()