def generate_palette(season):

    palettes = {

        "Bright Spring": ["#FF5A36","#FFD700","#00FA9A","#FF69B4","#FFA07A",
                         "#FF4500","#7FFF00","#FF7F50","#FFD27F","#FFB347",
                         "#F4C542","#E3A857","#FFE066","#C1FF72","#FF8C42",
                         "#FF6F61","#FFCC33","#FFE135","#BFFF00","#FF9966"],

        "Light Spring": ["#FFE4B5","#FFF1CC","#FFDAB9","#FFFACD","#FDEBD0",
                         "#F9E79F","#FFEBCD","#FFF5EE","#FAF0BE","#FFF8DC",
                         "#FFEFD5","#F5DEB3","#FFE4E1","#FFF0F5","#FFE4C4",
                         "#FFFACD","#FFF5E1","#FDF5E6","#FFF8DC","#FFEBCD"],

        "Soft Summer": ["#A8B5C0","#C3CED6","#E0E6EB","#8FA3B0","#B0C4CF",
                        "#D6DEE3","#7C8B97","#F2F4F6","#6D7C88","#9FB3C1",
                        "#BCC9D2","#D9E1E8","#A5B6C2","#D0D9E0","#E8EEF2",
                        "#B7C6D1","#90A4AE","#C7D3DB","#8395A7","#E3E8EC"],

        "Soft Autumn": ["#A67B5B","#C2A083","#E6C7A8","#8B6F47","#B08968",
                        "#DDB892","#7F5539","#F5E6CC","#6B4F4F","#C9A27E",
                        "#A38F85","#EAD2AC","#9C6644","#B7B7A4","#D4A373",
                        "#F0E2D0","#5C3D2E","#E0C097","#8D6E63","#F3D5B5"],

        "Deep Autumn": ["#3B2F2F","#5C4033","#6B4423","#8B5E3C","#A0522D",
                        "#4E342E","#3E2723","#7B3F00","#5D3A00","#6E260E",
                        "#8D6E63","#4A2C2A","#7C4A3A","#6D4C41","#5A3E36",
                        "#4B2E2A","#7A4E3A","#6A3E2E","#5B3428","#3C2A21"],

        "True Winter": ["#000000","#FFFFFF","#FF0000","#0000FF","#00FF00",
                        "#FF00FF","#00FFFF","#1C1C1C","#2F2F2F","#3A3A3A",
                        "#DC143C","#0033CC","#8A2BE2","#00CED1","#FF1493",
                        "#191970","#2B2B2B","#6600CC","#0099FF","#FF2D2D"],

        "Bright Winter": ["#FFFFFF","#000000","#FF0000","#0000FF","#00FF00",
                          "#FF00FF","#00FFFF","#DC143C","#1E90FF","#7FFF00",
                          "#FF1493","#00CED1","#8A2BE2","#FF4500","#00BFFF",
                          "#2F2F2F","#191970","#FF2D2D","#00FF7F","#6600CC"]
    }

    return palettes.get(season, palettes["Soft Autumn"])
