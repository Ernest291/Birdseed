"""
This module contains ASCII/ANSI arts.

"""

# from colors import *
from .colors import *
#example 
def show_status():
    print(f"{BG_PURPLE}{BRIGHT_WHITE} Highlighted Banner {RESET}")

def win_ascii():
    YOU_WIN = r"""
__   __ ___   _   _    __        __ ___  _   _  _ 
\ \ / // _ \ | | | |   \ \      / /|_ _|| \ | || |
 \ V /| | | || | | |    \ \ /\ / /  | | |  \| || |
  | | | |_| || |_| |     \ V  V /   | | | |\  ||_|
  |_|  \___/  \___/       \_/\_/   |___||_| \_|(_)
    """
    print(YOU_WIN)

def lose_ascii():
    YOU_LOSE = r"""
__   __ ___   _   _     _      ___   ____   _____  _ 
\ \ / // _ \ | | | |   | |    / _ \ / ___| | ____|| |
 \ V /| | | || | | |   | |   | | | |\___ \ |  _|  | |
  | | | |_| || |_| |   | |___| |_| | ___) || |___ |_|
  |_|  \___/  \___/    |_____|\___/ |____/ |_____|(_)
    """
    print(YOU_LOSE)

""" ----------------------------------------------------
STAGE 1
    ----------------------------------------------------
""" 


vsGnome = f"""    
                                      {YELLOW}/\\{RESET}
    {RED}  .--. {RESET}                          {YELLOW}/  \\{RESET}
    {RED}   (  o > {RESET}                      {YELLOW}/____\\{RESET}
    {RED}   /  ._)  {RESET}                     (o..o)
    {RED}   /__.'    {RESET}                     \\__/
        ||                           /  \\
"""
vsButterfly = f"""
    {RED}  .--. {RESET}                             {MAGENTA}\\  /{RESET}
    {RED}   (  o > {RESET}                        {BRIGHT_MAGENTA}(  |  ){RESET}
    {RED}   /  ._)  {RESET}                       {MAGENTA} ( | ){RESET}
    {RED}   /__.'    {RESET}
        ||
"""
vsFlower = f"""
    {RED}  .--. {RESET}                              {PINK}.{LAVENDER}-{PINK}.{RESET}
    {RED}   (  o > {RESET}                          {GOLD}({BRIGHT_YELLOW} * {GOLD}){RESET}
    {RED}   /  ._)  {RESET}                          {MAGENTA}'{PINK}-{MAGENTA}'{RESET}
    {RED}   /__.'    {RESET}                         {LIME}\\{GREEN}|{MINT}/{RESET}
        ||                                {GREEN}|{RESET}
"""
vsSnail = f"""
    {RED}  .--. {RESET}                      {YELLOW}@   @{RESET}   {CORAL}.----.{RESET}
    {RED}   (  o > {RESET}                     {GOLD}\\v/{RESET}  {PINK}.`{GOLD}.-"-.{PINK} \\{RESET}
    {RED}   /  ._)  {RESET}                    {GOLD}( \\_ / {PINK}/ '/ | |{RESET}
    {RED}   /__.'    {RESET}                     {GOLD}\\  .\\{PINK} .-' /-,{RESET}
        ||                           {GOLD}`----{PINK}`----'---'{RESET}
"""
vsBees = f"""
    {RED}  .--. {RESET}                                 {BRIGHT_YELLOW}\\ /{RESET}
    {RED}   (  o > {RESET}                            {GOLD}-({BRIGHT_YELLOW}|||{GOLD})-{BRIGHT_CYAN}o{RESET}   {BRIGHT_YELLOW}\\ /{RESET}
    {RED}   /  ._)  {RESET}                                   {GOLD}-({BRIGHT_YELLOW}|||{GOLD})-{BRIGHT_CYAN}o{RESET}
    {RED}   /__.'    {RESET}
        ||
"""
vsEarthworm = f"""
    {RED}  .--. {RESET}                        {CORAL}_     _   {PINK}.-.{RESET}
    {RED}   (  o > {RESET}                     {CORAL}.' '. .' '.{PINK}  o){RESET}
    {RED}   /  ._)  {RESET}                    {PINK}~'{CORAL}   '-'{PINK}   '---'{RESET}
    {RED}   /__.'    {RESET}
        ||
"""
vsCat = f"""
    {RED}  .--. {RESET}                                   {GOLD}/\\_/\\{RESET}
    {RED}   (  o > {RESET}                               {GOLD}( {PINK}-.-{GOLD} ){RESET}
    {RED}   /  ._)  {RESET}                              {ORANGE}/     \\  {GRAY}_{RESET}
    {RED}   /__.'    {RESET}                            {ORANGE}(       ){GRAY}/ ){RESET}
        ||                                   {GRAY}\\_|_|_/(_/{RESET}
"""
vsScarecrow = f"""
    {RED}  .--. {RESET}                                       {GOLD}/\\{RESET}
    {RED}   (  o > {RESET}                                   {GOLD}({BRIGHT_RED}xx{GOLD}){RESET}
    {RED}   /  ._)  {RESET}                                 {CORAL}-|{GOLD}__{CORAL}|-{RESET}
    {RED}   /__.'    {RESET}                                  {GOLD}||{RESET}
        ||
"""
vsQueenbee = f"""
                                        {BRIGHT_YELLOW}\\  {GOLD}v{BRIGHT_YELLOW}  /{RESET}
                                         {GOLD}\\_|_{GOLD}/{RESET}
    {RED}  .--. {RESET}                          {PINK}.--{GOLD}( {BRIGHT_WHITE}😳 {GOLD}){PINK}--.{RESET}
    {RED}   (  o > {RESET}                     {PINK}/  {GOLD}/ \\ V / \\  {PINK}\\  \\{RESET}
    {RED}   /  ._)  {RESET}                    {PINK}'-'{GOLD}  /==={GOLD}  {PINK}'-'{RESET}
    {RED}   /__.'    {RESET}                       {GOLD}/ [{BRIGHT_CYAN}o{GOLD}] \\{RESET}
        ||                            {GOLD}/======={RESET}
                                      {GOLD}| [{BRIGHT_CYAN}o{GOLD}] [{BRIGHT_CYAN}o{GOLD}] |{RESET}
 {GOLD}\\_______/{RESET}
 """

""" 
STAGE 2
"""
vsCatterpillar = f"""
    {RED}  .--. {RESET}                                    {LIME}\\ /{RESET}
    {RED}   (  o > {RESET}                              {GREEN}_ _ _{LIME}({BRIGHT_YELLOW}o{LIME}){RESET}
    {RED}   /  ._)  {RESET}                             {GREEN}((_(_(){RESET}
    {RED}   /__.'    {RESET}
        ||
"""
vsSquirrel = f"""
    {RED}  .--. {RESET}                              {CORAL}(\\_/){GRAY}    .-.{RESET}
    {RED}   (  o > {RESET}                            {CORAL}(o.o){GRAY}   /   ){RESET}
    {RED}   /  ._)  {RESET}                          {CORAL}(> {GOLD}@{CORAL} <){GRAY} (   /{RESET}
    {RED}   /__.'    {RESET}                         {CORAL}(     ){GRAY}  \\ /{RESET}
        ||                                  {CORAL}\\___/{GRAY}----'{RESET}
"""
vsStickinsect = f"""
                                      {GREEN}\\   \\    /{RESET}
                                       {LIME}\\   \\  /{RESET}
    {RED}  .--. {RESET}
    {RED}   (  o > {RESET}                       {GREEN}---{LIME}({BRIGHT_YELLOW}o{LIME}){GREEN}=========={RESET}
    {RED}   /  ._)  {RESET}
    {RED}   /__.'    {RESET}                       {LIME}/   /  \\{RESET}
        ||                              {GREEN}/   /    \\{RESET}
"""
vsMantis = f"""
                                         {LIME}\\ /{RESET}
    {RED}  .--. {RESET}                           {LIME}({BRIGHT_YELLOW}o{GREEN}V{BRIGHT_YELLOW}o{LIME}){RESET}
    {RED}   (  o > {RESET}                        {GREEN}/_|__{RESET}
    {RED}   /  ._)  {RESET}                       {LIME}' {GREEN}/====>{RESET}
    {RED}   /__.'    {RESET}                      {LIME}/ /  \\{RESET}
        ||
"""
vsFirefly = f"""
    {RED}  .--. {RESET}                             {BRIGHT_YELLOW}\\ /{RESET}
    {RED}   (  o > {RESET}                       {GOLD}o--{BRIGHT_YELLOW}(*){RESET}
    {RED}   /  ._)  {RESET}                         {BRIGHT_YELLOW}/ \\{RESET}
    {RED}   /__.'    {RESET}                       
        ||
"""
vsTreant = f"""
                                         {CORAL}. ~ ~ ~ ~ .{RESET}
                                     {CORAL}.~({BRIGHT_YELLOW}  ~  @  ~  {CORAL}).~.{RESET}
                                    {CORAL}( ~   ~      ~   ~ ){RESET}
    {RED}  .--. {RESET}                          {CORAL}'._  {BRIGHT_YELLOW}~  @  ~  {CORAL}_.'{RESET}
    {RED}   (  o > {RESET}                          {GOLD}|{GRAY}  _     _  {GOLD}|{RESET}
    {RED}   /  ._)  {RESET}                         {GOLD}|{GRAY} ({BRIGHT_CYAN}O{GRAY})   ({BRIGHT_CYAN}O{GRAY}) {GOLD}|{RESET}
    {RED}   /__.'    {RESET}                        {GOLD}|{GRAY}    /_\\    {GOLD}|{RESET}
        ||                              {GOLD}|{GRAY}    ({BRIGHT_CYAN}O{GRAY})    {GOLD}|{RESET}
                                       {GOLD}/|{GRAY}           {GOLD}|\\{RESET}
                                      {GOLD}/_|___________|_\\{RESET}
"""
vsFlyingsquirrel = f"""
                                      {CORAL}(\\_/){RESET}
                                    {GOLD}--{CORAL}({BRIGHT_CYAN}o{CORAL}.{BRIGHT_CYAN}o{CORAL}){GOLD}--{RESET}
                                  {CORAL}/  \\     /  \\{RESET}
    {RED}  .--. {RESET}                      {CORAL}(    {GOLD}|   |{CORAL}    ){RESET}
    {RED}   (  o > {RESET}                    {CORAL}\\__/{GOLD}|___|{CORAL}\\__/{RESET}
    {RED}   /  ._)  {RESET}                      {CORAL}/     \\{RESET}
        ||                           {CORAL})     ({RESET}
                                     {CORAL}(     ){RESET}
                                      {CORAL}'---'{RESET}
"""
vsAspid = f"""
                                         {BRIGHT_YELLOW}\\ /{RESET}
                                        {GOLD}({BRIGHT_WHITE}😳{GOLD}){RESET}
    {RED}  .--. {RESET}                           {GOLD}--{CORAL}/|\\{GOLD}--{RESET}
    {RED}   (  o > {RESET}                        {CORAL}.-' '-.{RESET}
    {RED}   /  ._)  {RESET}                      {CORAL}(   {BRIGHT_CYAN}~   {CORAL}){RESET}
    {RED}   /__.'    {RESET}                     {CORAL}'-.____.-'{RESET}
        ||
"""
""" 
STAGE 3 
"""
vsCrab = f"""
                                      {GOLD}..         ..{RESET}
                                    {GOLD}(  _ \\       / _  ){RESET}
                                     {GOLD}'-.\\ \\ _ / /.-'{RESET}
    {RED}  .--. {RESET}                            {GOLD}.'-({BRIGHT_CYAN}o o{GOLD})-'.{RESET}
    {RED}   (  o > {RESET}                       {CORAL}/  {GOLD}.-------.  {CORAL}\\{RESET}
    {RED}   /  ._)  {RESET}                     {CORAL}/ \\_/{GOLD}         {CORAL}\\_/ \\{RESET}
    {RED}   /__.'    {RESET}                   {CORAL}/   / {GOLD}'---------' {CORAL}\\   \\{RESET}
        ||                         {CORAL}'   '             '   '{RESET}
"""
vsFlyingfish  = f"""
                                        {BRIGHT_CYAN}_.-.{RESET}
                                      {BRIGHT_CYAN}.'    \\{RESET}
    {RED}  .--. {RESET}                        {GOLD}<{BRIGHT_CYAN}({BRIGHT_YELLOW}o{BRIGHT_CYAN}){GOLD}====={BRIGHT_CYAN}><{RESET}
    {RED}   (  o > {RESET}                      {BRIGHT_CYAN}'.    /{RESET}
    {RED}   /  ._)  {RESET}                        {BRIGHT_CYAN}'-'{RESET}
    {RED}   /__.'    {RESET}
        ||
"""
vsAlbatross = f"""
                                      {CORAL}   _     _{RESET}
    {RED}  .--. {RESET}                          {CORAL}  /  \\.-./  \\{RESET}
    {RED}   (  o > {RESET}                       {CORAL} /    `-'    \\{RESET}
    {RED}   /  ._)  {RESET}                      {CORAL}'             '{RESET}
    {RED}   /__.'    {RESET}
        ||
"""
vsSeagull = f"""
                                         {BRIGHT_CYAN}_.-.{RESET}
                                        {BRIGHT_CYAN}.'  {BRIGHT_YELLOW}o {BRIGHT_CYAN}'--{RESET}
    {RED}  .--. {RESET}                             {BRIGHT_CYAN}/   /{RESET}
    {RED}   (  o > {RESET}                         {BRIGHT_CYAN}/   /____{RESET}
    {RED}   /  ._)  {RESET}                       {BRIGHT_CYAN}(    \\    '---._{RESET}
    {RED}   /__.'    {RESET}                        {BRIGHT_CYAN}'-.  '-._____.-'{RESET}
        ||                                  {BRIGHT_CYAN}'-. {GOLD}|   {BRIGHT_CYAN}{RESET}
                                               {GOLD}||{RESET}
                                               {GOLD}||{RESET}
"""
vsLighthouse = f"""
                                           {BRIGHT_YELLOW}^{RESET}
                                          {GOLD}/ \\{RESET}
    {RED}  .--. {RESET}                            {BRIGHT_CYAN}- {GOLD}| {BRIGHT_YELLOW}* {GOLD}| {BRIGHT_CYAN}-{RESET}
    {RED}   (  o > {RESET}                           {GOLD}|___|{RESET}
    {RED}   /  ._)  {RESET}                          {GOLD}|   |{RESET}
    {RED}   /__.'    {RESET}                         {GOLD}| {BRIGHT_CYAN}o {GOLD}|{RESET}
        ||                              {GOLD}/_____\\{RESET}
                                      {BRIGHT_CYAN}~~~~~~~{RESET}
"""
vsPelican = f"""
                                        {BRIGHT_CYAN}_.-.{RESET}
                                      {BRIGHT_CYAN}.'  {BRIGHT_YELLOW}o {BRIGHT_CYAN}'-.______{RESET}
    {RED}  .--. {RESET}                           {BRIGHT_CYAN}/   /    `------'{RESET}
    {RED}   (  o > {RESET}                       {BRIGHT_CYAN}(    \\__________.'{RESET}
    {RED}   /  ._)  {RESET}                        {BRIGHT_CYAN}'-.______.-'{RESET}
        ||                                  {GOLD}||  ||{RESET}
"""
vsNemo = f"""
                                                 {CORAL}.-.{RESET}
                                        {CORAL}.-' {BRIGHT_WHITE}| | {CORAL}'-.   {CORAL}/|{RESET}
    {RED}  .--. {RESET}                           {CORAL}.'  {BRIGHT_YELLOW}o {BRIGHT_WHITE}| |  {CORAL}| {BRIGHT_WHITE}'.'{CORAL} |{RESET}
    {RED}   (  o > {RESET}                       {CORAL}(      {BRIGHT_WHITE}| |  {CORAL}|     |{RESET}
    {RED}   /  ._)  {RESET}                       {CORAL}'.___ {BRIGHT_WHITE}| |  {CORAL}| {BRIGHT_WHITE}.'.'{CORAL} |{RESET}
        ||                                   {BRIGHT_WHITE}'-'-'{CORAL}    {CORAL}\\|{RESET}
"""
""" 
STAGE 4
"""

vsHornets = f"""
                                      {BRIGHT_YELLOW}\\ /{RESET}
    {RED}  .--. {RESET}                        {GOLD}o-{BRIGHT_YELLOW}({GRAY}|||{BRIGHT_YELLOW}){GOLD}>-{RESET}   {BRIGHT_YELLOW}\\ /{RESET}
    {RED}   (  o > {RESET}                                 {GOLD}o-{BRIGHT_YELLOW}({GRAY}|||{BRIGHT_YELLOW}){GOLD}>-{RESET}
    {RED}   /  ._)  {RESET}
    {RED}   /__.'    {RESET}
        ||
"""
vsMountaingoat = f"""
                                    {BRIGHT_WHITE}(\\(\\ {RESET}
    {RED}  .--. {RESET}                          {BRIGHT_WHITE}( {BRIGHT_YELLOW}o{BRIGHT_WHITE}_.-'-.{RESET}
    {RED}   (  o > {RESET}                         {BRIGHT_WHITE}\\|      \\~{RESET}
    {RED}   /  ._)  {RESET}                         {GOLD}||{BRIGHT_WHITE}----{GOLD}||{RESET}
    {RED}   /__.'    {RESET}                        {GOLD}||{BRIGHT_WHITE}    {GOLD}||{RESET}
        ||
"""
vsPebblit = f"""
                                     {GRAY}_.---.{RESET}
    {RED}  .--. {RESET}                        {GRAY}.'      '.{RESET}
    {RED}   (  o > {RESET}                     {BRIGHT_WHITE}[_{GRAY}|      |{BRIGHT_WHITE}_]{RESET}
    {RED}   /  ._)  {RESET}                      {GRAY}'.____.'{RESET}
    {RED}   /__.'    {RESET}                      {BRIGHT_WHITE}[_][_]{RESET}
        ||
"""
vsRaven = f"""
                                        {BRIGHT_WHITE}_{RESET}
    {RED}  .--. {RESET}                           {BRIGHT_WHITE}({BRIGHT_YELLOW}o{BRIGHT_WHITE})>{RESET}
    {RED}   (  o > {RESET}                         {GRAY}//{BRIGHT_WHITE}\\{RESET}
    {RED}   /  ._)  {RESET}                        {GRAY}V_/__{RESET}
        ||
"""
vsHoneyguide = f"""
                                      {GOLD}.-._ {RESET}
    {RED}  .--. {RESET}                           {BRIGHT_YELLOW}<  {BRIGHT_WHITE}o {GOLD}){RESET}
    {RED}   (  o > {RESET}                         {GOLD}\\_=  \\{RESET}
    {RED}   /  ._)  {RESET}                           {BRIGHT_YELLOW}-||--'{RESET}
    {RED}   /__.'    {RESET}
        ||
"""
vsPou = f"""
                                     {GOLD}()_(){RESET}
    {RED}  .--. {RESET}                         {GOLD}/ {BRIGHT_WHITE}o o {GOLD}\\{RESET}
    {RED}   (  o > {RESET}                      {BRIGHT_YELLOW}(()){GOLD}   \\{RESET}
    {RED}   /  ._)  {RESET}                    {GOLD}/ {CORAL},==.   {GOLD}\\{RESET}
    {RED}   /__.'    {RESET}                  {GOLD}(  {CORAL}|__|    {GOLD}){RESET}
        ||                         {GOLD}\\ {BRIGHT_YELLOW}(  '.__){RESET}
                                  {BRIGHT_YELLOW}(((_.-(((_ {RESET}
"""
vsMaurice = f"""
                                      {BRIGHT_CYAN}_--------.{RESET}
                                 {BRIGHT_CYAN}_--/  {GOLD}// // / /{RESET}
    {RED}  .--. {RESET}                   {BRIGHT_YELLOW}<    {BRIGHT_WHITE}-o-      {BRIGHT_CYAN}.'{GOLD}==={RESET}
    {RED}   (  o > {RESET}                  {BRIGHT_CYAN}'-----.     /{RESET}
    {RED}   /  ._)  {RESET}                        {BRIGHT_CYAN}/   .'{RESET}
    {RED}   /__.'    {RESET}                     {GOLD}-=--'{RESET}
        ||
"""
# print(vsHornets)
# print(vsMountaingoat)
# print(vsPebblit)
# print(vsRaven)
# print(vsHoneyguide)
# print(vsPou)
# print(vsMaurice)
