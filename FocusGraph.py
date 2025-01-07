import matplotlib.pyplot as plt

def focus_graph():
    try:
        with open('data/focus.txt', 'r') as file:
            content = file.read()
            
        if not content.strip():
            print("No focus data available yet. Use focus mode first.")
            return
            
        data = [float(x) for x in content.split(',') if x.strip()]
        
        plt.figure(figsize=(10, 6))
        plt.plot(data, color='red', marker='o')
        plt.title("Your Focus Time", fontsize=16)
        plt.xlabel("Sessions", fontsize=14)
        plt.ylabel("Minutes", fontsize=14)
        plt.grid(True)
        plt.show()
        
    except FileNotFoundError:
        print("No focus data found. Use focus mode first.")
    except Exception as e:
        print(f"Error displaying focus graph: {e}")