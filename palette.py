def generate_palette(season):

    palettes = {

        # 🌸 SPRING (4)
        "Bright Spring": ["#FF5A36","#FFD700","#00FA9A","#FF69B4","#FFA07A","#FFB347","#FF7F50","#7FFF00","#FFE066","#FF9966"],

        "Light Spring": ["#FFF1CC","#FFE4B5","#FFFACD","#FFEBCD","#FDEBD0","#FFF5E1","#FAF0BE","#FFEFD5","#FFF8DC","#F5DEB3"],

        "Soft Spring": ["#FAD7A0","#F5CBA7","#F8C471","#F0B27A","#E59866","#DC7633","#F7DC6F","#F9E79F","#FDEBD0","#E6B0AA"],

        "Warm Spring": ["#FFAA33","#FFCC66","#FF9966","#FFD27F","#FFB84D","#F4C542","#E3A857","#FFCC99","#E6A44C","#FF9F1C"],

        # ☀️ SUMMER (3)
        "Light Summer": ["#DCE6F1","#E3EDF7","#BFD7EA","#C9D6DF","#A9BCD0","#EAF2F8","#D0E1F9","#B8C6D1","#E5ECF4","#C3D3E3"],

        "Soft Summer": ["#A8B5C0","#C3CED6","#E0E6EB","#8FA3B0","#B0C4CF","#D6DEE3","#7C8B97","#F2F4F6","#6D7C88","#9FB3C1"],

        "True Summer": ["#6FA3EF","#A7C7E7","#C3D9F1","#8BB8D4","#B0D0E8","#D0E4F5","#7A9CC6","#E6F0FA","#5F7FA3","#9CBEDC"],

        # 🍂 AUTUMN (4)
        "Soft Autumn": ["#A67B5B","#C2A083","#E6C7A8","#8B6F47","#B08968","#DDB892","#7F5539","#F5E6CC","#6B4F4F","#C9A27E"],

        "Muted Autumn": ["#A38F85","#B7A99A","#C9B8A8","#8C7B75","#B5A69A","#D2C1B0","#7E6C63","#E3D5C9","#6F5F57","#A4948A"],

        "Deep Autumn": ["#3B2F2F","#5C4033","#6B4423","#8B5E3C","#A0522D","#4E342E","#3E2723","#7B3F00","#5D3A00","#6E260E"],

        "True Autumn": ["#8B4000","#A0522D","#CD853F","#D2691E","#B5651D","#6E260E","#7B3F00","#8B5A2B","#C68642","#D2B48C"],

        # ❄️ WINTER (5)
        "Bright Winter": ["#FFFFFF","#000000","#FF0000","#0000FF","#00FF00","#FF00FF","#00FFFF","#DC143C","#1E90FF","#7FFF00"],

        "Cool Winter": ["#0A0A0A","#FFFFFF","#1E90FF","#4682B4","#7B68EE","#8A2BE2","#4169E1","#00BFFF","#2F4F4F","#708090"],

        "Deep Winter": ["#000000","#1A1A1A","#2B2B2B","#3C3C3C","#4D4D4D","#660000","#003366","#000080","#2E0854","#191970"],

        "True Winter": ["#000000","#FFFFFF","#FF0000","#0000FF","#00FF00","#FF00FF","#00FFFF","#8B0000","#000080","#191970"]
    }

    return palettes.get(season, palettes["Soft Autumn"])
