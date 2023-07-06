"""
    
    PyeMenu version 1.0.0
    This module contain the color value.

    This module was developed by Freire Alexander Palomino Palma
    *Copyright (c) 2014-2023 Freire Alexander Palomino Palma*
"""

# SGR color constants
# rene-d 2018
not_fg = '\x1b[39m'
not_bg = '\x1b[49m'

def setColor(color: str):
    """
    This function allow to transform html color to the format needed
    """
    if color == not_fg:
        return not_fg
    elif color == not_bg:
        return not_bg
    else:
        hex = color.lstrip('#')
        color = ";".join([str(int(hex[i:i+2], 16)) for i in (0, 2, 4)])
        color = "2;"+color+"m"
        return color

def html_rgb_fg(color: str):
    """
    This function allow to transform html color to the format needed
    """
    if color == not_fg:
        return not_fg
    else:
        hex = color.lstrip('#')
        color = ";".join([str(int(hex[i:i+2], 16)) for i in (0, 2, 4)])
        color = "\x1b[38;2;"+color+"m"
        return color

def html_rgb_bg(color: str):
    """
    This function allow to transform html color to the format needed
    """
    if color == not_bg:
        return not_bg
    else:
        hex = color.lstrip('#')
        color = ";".join([str(int(hex[i:i+2], 16)) for i in (0, 2, 4)])
        color = "\x1b[48;2;"+color+"m"
        return color


class Colors:
    """
    This Class contains a large list with html colors by its name
    Color By Names from https://htmlcolorcodes.com/color-names/
    """
    white=                       '#ffffff'
    black=                       '#000000'
    gray=                        '#696969'
    yellow=                      '#ffff00'
    red=                         '#ff0000'
    green=                       '#008000'
    blue=                        '#0000ff'
    orange=                      '#ffa500'
    purple=                      '#800080'
    brown=                       '#a52a2a'
    pink=                        '#ffc0cb'
    # Red HTML Color Names 
    IndianRed=                   '#CD5C5C'
    LightCoral=                	 '#F08080'
    Salmon=     	             '#FA8072'
    DarkSalmon=                  '#E9967A'	
    LightSalmon=                 '#FFA07A'	
    Crimson=                     '#DC143C'	 
    FireBrick=                   '#B22222'	
    DarkRed=                     '#8B0000'	
    # Pink HTML Color Names 
    LightPink=	                 '#FFB6C1'
    HotPink=                     '#FF69B4'
    DeepPink=	                 '#FF1493'
    MediumVioletRed=             '#C71585'
    PaleVioletRed=	             '#DB7093'
    # Orange HTML Color Names 
    LightSalmon=                '#FFA07A'	
    Coral=                      '#FF7F50'	
    Tomato=                     '#FF6347'	
    OrangeRed=                  '#FF4500'	
    DarkOrange=                 '#FF8C00'
    # Yellow HTML Color Names 
    Gold=                   	'#FFD700'
    LightYellow=                '#FFFFE0'
    LemonChiffon=               '#FFFACD'
    LightGoldenrodYellow=       '#FAFAD2'
    PapayaWhip=                 '#FFEFD5'
    Moccasin=                   '#FFE4B5'
    PeachPuff=                  '#FFDAB9'
    PaleGoldenrod=              '#EEE8AA'
    Khaki=                  	'#F0E68C'
    DarkKhaki=                  '#BDB76B'
    # Purple HTML Color Names 
    Lavender=	                '#E6E6FA'
    Thistle=	                '#D8BFD8'
    Plum=	                    '#DDA0DD'
    Violet=	                    '#EE82EE'
    Orchid=	                    '#DA70D6'
    Fuchsia=	                '#FF00FF'
    Magenta=	                '#FF00FF'
    MediumOrchid=	            '#BA55D3'
    MediumPurple=	            '#9370DB'
    RebeccaPurple=	            '#663399'
    BlueViolet=	                '#8A2BE2'
    DarkViolet=	                '#9400D3'
    DarkOrchid=	                '#9932CC'
    DarkMagenta=	            '#8B008B'
    Indigo=	                    '#4B0082'
    SlateBlue=	                '#6A5ACD'
    DarkSlateBlue=	            '#483D8B'
    MediumSlateBlue=	        '#7B68EE'
    # Green HTML Color Names 
    GreenYellow=                '#ADFF2F'
    Chartreuse=                 '#7FFF00'
    LawnGree=                   '#7CFC00'
    Lime=                       '#00FF00'
    LimeGreen=                  '#32CD32'
    PaleGreen=                  '#98FB98'
    LightGreen=                 '#90EE90'
    MediumSpringGreen=          '#00FA9A'
    SpringGreen=                '#00FF7F'
    MediumSeaGreen=             '#3CB371'
    SeaGreen=                   '#2E8B57'
    ForestGreen=                '#228B22'
    DarkGreen=                  '#006400'
    YellowGreen=                '#9ACD32'
    OliveDrab=                  '#6B8E23'
    Olive=                      '#808000'
    DarkOliveGreen=             '#556B2F'
    MediumAquamarine=           '#66CDAA'
    DarkSeaGreen=               '#8FBC8B'
    LightSeaGreen=              '#20B2AA'
    DarkCyan=                   '#008B8B'
    Teal=                       '#008080'
    # Blue HTML Color Names 
    Cyan=                   	'#00FFFF'
    LightCyan=                  '#E0FFFF'
    PaleTurquoise=              '#AFEEEE'
    Aquamarine=                 '#7FFFD4'
    Turquoise=                  '#40E0D0'
    MediumTurquoise=            '#48D1CC'
    DarkTurquoise=              '#00CED1'
    CadetBlue=                  '#5F9EA0'
    SteelBlue=                  '#4682B4'
    LightSteelBlue=             '#B0C4DE'
    PowderBlue=                 '#B0E0E6'
    LightBlue=                  '#ADD8E6'
    SkyBlue=                    '#87CEEB'
    LightSkyBlue=               '#87CEFA'
    DeepSkyBlue=                '#00BFFF'
    DodgerBlue=                 '#1E90FF'
    CornflowerBlue=             '#6495ED'
    MediumSlateBlue=            '#7B68EE'
    RoyalBlue=                  '#4169E1'
    MediumBlue=                 '#0000CD'
    DarkBlue=                   '#00008B'
    Navy=                   	'#000080'
    MidnightBlue=               '#191970'
    # Brown HTML Color Names 
    Cornsilk=                   '#FFF8DC'
    BlanchedAlmond=             '#FFEBCD'
    Bisque=                 	'#FFE4C4'
    NavajoWhite=                '#FFDEAD'
    Wheat=                  	'#F5DEB3'
    BurlyWood=                  '#DEB887'
    Tan=                    	'#D2B48C'
    RosyBrown=                  '#BC8F8F'
    SandyBrown=                 '#F4A460'
    Goldenrod=                  '#DAA520'
    DarkGoldenrod=              '#B8860B'
    Peru=                   	'#CD853F'
    Chocolate=                  '#D2691E'
    SaddleBrown=                '#8B4513'
    Sienna=                 	'#A0522D'
    Maroon=                 	'#800000'
    #  White HTML Color Names 
    Snow=                   	'#FFFAFA'
    HoneyDew=                   '#F0FFF0'
    MintCream=                  '#F5FFFA'
    Azure=                  	'#F0FFFF'
    AliceBlue=                  '#F0F8FF'
    GhostWhite=                 '#F8F8FF'
    WhiteSmoke=                 '#F5F5F5'
    SeaShell=                   '#FFF5EE'
    Beige=                  	'#F5F5DC'
    OldLace=                    '#FDF5E6'
    FloralWhite=                '#FFFAF0'
    Ivory=                  	'#FFFFF0'
    AntiqueWhite=               '#FAEBD7'
    Linen=                  	'#FAF0E6'
    LavenderBlush=              '#FFF0F5'
    MistyRose=                  '#FFE4E1'
    # Gray HTML Color Names 
    Gainsboro=                  '#DCDCDC'
    LightGray=                  '#D3D3D3'
    Silver=                 	'#C0C0C0'
    DarkGray=                   '#A9A9A9'
    DimGray=                    '#696969'
    LightSlateGray=             '#778899'
    SlateGray=                  '#708090'
    DarkSlateGray=              '#2F4F4F'
    # Blacks HTML Color Names
    BlackOlive=                 '#3B3C36'
    Onyx=                       '#353839'
    Jet=                        '#343434'
    JetBlack=                   '#0E0E10'