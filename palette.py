def generate_palette(hex_color):
    """
    Verilen ana renkten 5 uyumlu renk paleti oluşturur.
    #FF5733 -> ['#FF5733', '#FF7A33', '#FFA033', ...]
    """
    hex_color = hex_color.lstrip('#')
    r, g, b = tuple(int(hex_color[i:i+2], 16) for i in range(0, 6, 2))
    
    palette = [f'#{hex_color.upper()}']
    
    # Açık tonlar ekle
    for i in range(1, 5):
        new_r = min(255, r + i * 20)
        new_g = min(255, g + i * 15) 
        new_b = min(255, b + i * 10)
        palette.append(f'#{new_r:02X}{new_g:02X}{new_b:02X}')
        
    return palette

# Test et
if __name__ == "__main__":
    renk = "#FF5733"  # Turuncu
    print("Paletin:", generate_palette(renk))
