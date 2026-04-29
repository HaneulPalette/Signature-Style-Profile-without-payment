def generate_palette(season):

    palettes = {

        # 🌸 SPRING FAMILY
        "Bright Spring": [
            "#FF5A36","#FFB347","#FFD700","#7FFF00","#00FA9A",
            "#FF69B4","#FFA07A","#FF4500","#FF7F50","#FFD27F",
            "#F4C542","#E3A857","#FFCC99","#FF9F1C","#FFE066",
            "#C1FF72","#FF6F61","#FFD1DC","#FFE135","#BFFF00",
            "#FF8C42","#E6C200","#F6B26B","#FFAA00","#FFD580"
        ],

        "Warm Spring": [
            "#FFAA33","#FFCC66","#FF9966","#FFD27F","#FFB84D",
            "#E6A44C","#FF8C42","#F4C542","#D98C2B","#FFB347",
            "#E3A857","#FFCC99","#E6B85C","#FF9F1C","#F2C14E",
            "#E89F3D","#FFD580","#FFAA00","#E6C200","#F6B26B",
            "#FFB266","#E6A23C","#FFD27F","#F4C542","#FFCC33"
        ],

        "Light Spring": [
            "#FFE5B4","#FFF1CC","#FFDAB9","#FFFACD","#FFE4E1",
            "#FDEBD0","#FAD7A0","#F9E79F","#FDEBD0","#F5DEB3",
            "#FFF5E1","#FFEBCD","#FFEFD5","#F0E68C","#FFF8DC",
            "#FAF0BE","#FFEFD5","#FDF5E6","#FFF0F5","#FAFAD2",
            "#FFE4B5","#FFFACD","#FFEBCD","#FFF5EE","#FFF8DC"
        ],

        "True Spring": [
            "#FF6F61","#FFB347","#FFD700","#32CD32","#00CED1",
            "#FF4500","#FFA500","#FFFF33","#7FFF00","#00FF7F",
            "#FF6347","#FFD27F","#FFAA00","#ADFF2F","#40E0D0",
            "#FF8C00","#FF69B4","#FFE135","#C1FF72","#FF7F50",
            "#FFD580","#E6C200","#F6B26B","#FF9966","#FFCC33"
        ],

        # ☀️ SUMMER FAMILY
        "Light Summer": [
            "#DCE6F1","#F1F5F9","#E3EDF7","#BFD7EA","#C9D6DF",
            "#EAF2F8","#A9BCD0","#F8FAFC","#D0E1F9","#B8C6D1",
            "#E5ECF4","#C3D3E3","#D9E2EC","#AFCBFF","#E0E8F0",
            "#F0F4F8","#C2D1E0","#D6E4F0","#B0C4DE","#E6EEF7",
            "#C7D7E0","#DDE6ED","#BFD0E1","#E9F1F7","#A7BED3"
        ],

        "Soft Summer": [
            "#A8B5C0","#C3CED6","#E0E6EB","#8FA3B0","#B0C4CF",
            "#D6DEE3","#7C8B97","#F2F4F6","#6D7C88","#9FB3C1",
            "#BCC9D2","#D9E1E8","#738491","#A5B6C2","#D0D9E0",
            "#E8EEF2","#5F6D78","#B7C6D1","#90A4AE","#C7D3DB",
            "#8395A7","#E3E8EC","#6A7B86","#A9BAC6","#DDE5EA"
        ],

        "True Summer": [
            "#6FA3EF","#A7C7E7","#C3D9F1","#8BB8D4","#B0D0E8",
            "#D0E4F5","#7A9CC6","#E6F0FA","#5F7FA3","#9CBEDC",
            "#C5D9F2","#DDEAF7","#6C8EBF","#A3C4F3","#D6E6F2",
            "#EAF2FB","#5A7BA8","#B3CDE3","#8FAADC","#CFE0F1",
            "#7FA6D8","#E3ECF7","#6B8FBF","#A9C3E8","#D5E4F2"
        ],

        "Muted Summer": [
            "#7C8B97","#8FA3B0","#A5B6C2","#B0C4CF","#6D7C88",
            "#9FB3C1","#C3CED6","#D9E1E8","#738491","#A9BAC6",
            "#BCC9D2","#DDE6ED","#5F6D78","#8395A7","#C7D3DB",
            "#E3E8EC","#6A7B86","#90A4AE","#B7C6D1","#D0D9E0",
            "#A8B5C0","#E8EEF2","#7C8B97","#B0C4CF","#D6DEE3"
        ],

        # 🍂 AUTUMN FAMILY
        "Soft Autumn": [
            "#A67B5B","#C2A083","#E6C7A8","#8B6F47","#B08968",
            "#DDB892","#7F5539","#F5E6CC","#6B4F4F","#C9A27E",
            "#A38F85","#EAD2AC","#9C6644","#B7B7A4","#D4A373",
            "#F0E2D0","#5C3D2E","#E0C097","#8D6E63","#F3D5B5",
            "#A98467","#6D4C41","#D7B49E","#C8A97E","#E1C699"
        ],

        "Deep Autumn": [
            "#3B2F2F","#5C4033","#6B4423","#8B5E3C","#A0522D",
            "#4E342E","#3E2723","#7B3F00","#5D3A00","#6E260E",
            "#8D6E63","#4A2C2A","#3D2B1F","#7C4A3A","#6D4C41",
            "#5A3E36","#4B2E2A","#7A4E3A","#6A3E2E","#5B3428",
            "#8C4F2F","#3C2A21","#7D4B3B","#6C3F31","#5D3326"
        ],

        "True Autumn": [
            "#8B4000","#A0522D","#CD853F","#D2691E","#B5651D",
            "#6E260E","#7B3F00","#8B5A2B","#A0522D","#C68642",
            "#D2B48C","#8C4F2F","#A9746E","#7A4E3A","#B87333",
            "#C19A6B","#6B4423","#8D6E63","#A67B5B","#5C4033",
            "#7C3F00","#9C661F","#D2691E","#8B4513","#C68642"
        ],

        "Muted Autumn": [
            "#A38F85","#B7A99A","#C9B8A8","#8C7B75","#B5A69A",
            "#D2C1B0","#7E6C63","#E3D5C9","#6F5F57","#A4948A",
            "#C7B7A3","#D8CAB9","#8A7A6F","#B3A497","#DCCCBF",
            "#E6D9CF","#6D5F57","#9B8A7E","#C2B2A3","#E1D2C5",
            "#A89A8E","#D5C6B8","#7F7066","#BCAEA0","#E8DCD1"
        ],

        # ❄️ WINTER FAMILY
        "Bright Winter": [
            "#000000","#FFFFFF","#FF0000","#0000FF","#00FF00",
            "#FF00FF","#00FFFF","#1C1C1C","#2F2F2F","#3A3A3A",
            "#E60026","#0033CC","#00BFFF","#8A2BE2","#DC143C",
            "#FFFFFF","#0F0F0F","#2B2B2B","#6600CC","#0099FF",
            "#FF1493","#00CED1","#191970","#FF2D2D","#00FF7F"
        ],

        "Cool Winter": [
            "#0A0A0A","#FFFFFF","#1E90FF","#4682B4","#5F9EA0",
            "#7B68EE","#8A2BE2","#4169E1","#6495ED","#87CEEB",
            "#B0E0E6","#E6E6FA","#2F4F4F","#708090","#778899",
            "#00BFFF","#1C1C1C","#2E2E2E","#3C3C3C","#4B4B4B",
            "#5A5A5A","#696969","#808080","#A9A9A9","#C0C0C0"
        ],

        "Deep Winter": [
            "#000000","#0B0B0B","#1A1A1A","#2B2B2B","#3C3C3C",
            "#4D4D4D","#5E5E5E","#6F6F6F","#808080","#999999",
            "#111111","#222222","#333333","#444444","#555555",
            "#660000","#003366","#000080","#8B0000","#2F2F2F",
            "#1C1C1C","#000000","#4B0082","#2E0854","#191970"
        ],

        "True Winter": [
            "#000000","#FFFFFF","#FF0000","#0000FF","#00FF00",
            "#FF00FF","#00FFFF","#8B0000","#000080","#191970",
            "#DC143C","#1E90FF","#00CED1","#FF1493","#7FFF00",
            "#FFFFFF","#0F0F0F","#2B2B2B","#6600CC","#0099FF",
            "#FF2D2D","#00FF7F","#2F2F2F","#1A1A1A","#3A3A3A"
        ]
    }

    return palettes.get(season, palettes["Soft Autumn"])
