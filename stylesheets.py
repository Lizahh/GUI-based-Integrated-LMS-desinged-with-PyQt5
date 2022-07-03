
color1 = "#7D4BB4"
color1mono = "#976FC3"
color1mono_dark = "#58357E"
color1_ = "#82B44B"
color1_mono = "#9BC36F"
color1_mono2 = "#DAE9CA"
main_style_sheet = f"""
    QMainWindow {{
        background-color:{color1_mono2};
    }}
    QPushButton {{
    font: 50 10pt "MS Sans Serif";
    background: {color1};
    color: white;
    border: 1px solid;
    border-radius: 2%;
   
    }}
    QPushButton:hover{{
    font: 50 10pt "MS Sans Serif";
    background: {color1mono};
    color: white;
    border: 1px solid;
    border-radius: 2%;
    }}
    QPushButton:hover:pressed{{
    font: 50 10pt "MS Sans Serif";
    background: {color1mono_dark};
    color: white;
    border: 1px solid;
    border-radius: 2%;
    }}
    QTabBar::tab:selected {{
        background: {color1};
        color: white;
        font: 200 15pt "MS Sans Serif";
        border: 1px solid;
        }}
    QTabBar::tab {{
        background: {color1_};
        width: 200%;
        height: 35%;
        font: 200 15pt "MS Sans Serif";
        }}
    QTabBar {{
        background: {color1_mono};
    }}
    QLabel {{
        font: 75 16pt "MS Sans Serif";
    }}
"""
dialog_style_sheet = f"""
QLabel#label{{
        font: 500 10pt "MS Sans Serif";
    }}

QDialog {{
        background-color:{color1_mono2};
}}
 QPushButton {{
    font: 50 10pt "MS Sans Serif";
    background: {color1};
    color: white;
    border: 1px solid;
    border-radius: 2%;
   
    }}
  QPushButton:hover{{
    font: 50 10pt "MS Sans Serif";
    background: {color1mono};
    color: white;
    border: 1px solid;
    border-radius: 2%;
    }}
    QPushButton:hover:pressed{{
    font: 50 10pt "MS Sans Serif";
    background: {color1mono_dark};
    color: white;
    border: 1px solid;
    border-radius: 2%;
    }}
"""

