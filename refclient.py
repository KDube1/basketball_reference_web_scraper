from basketball_reference_web_scraper import client
from basketball_reference_web_scraper.data import OutputType

print("This a user client for the basketball reference web scraper api by jaebradley https://github.com/jaebradley/basketball_reference_web_scraper")
print("This tool lets users easily obtain csv files of box scores for playoff games")
def writer(d,m,y):
    client.player_box_scores(day=d, month=m, year=y, output_type=OutputType.CSV, output_file_path="./"+str(d)+"_"+str(m)+"_"+str(y)+"_box_scores.csv")
    return None


d = int(input("Input day: ").strip())

m = int(input("Input month: ").strip())

y = int(input("Input year: ").strip())

writer(d,m,y)
    
