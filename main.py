import time
import argparse 


import gosat_module as gosat
import tansat_module as tansat
import oco2_module as oco2


def main():
    parser = argparse.ArgumentParser()
    #parser.add_argument('module', help='Спутник, с которым необходимо работать', choices=['GOSAT', 'OCO2', 'TANSAT'])
    parser.add_argument('--gosat', help='Получать данные со спутника GOSAT', action='store_true', default=False)
    parser.add_argument('--tansat', help='Получать данные со спутника TANSAT', action='store_true', default=False)
    parser.add_argument('--oco2', help='Получать данные со спутника OCO2', action='store_true', default=False)
    parser.add_argument('--update_time', help='Таймер проверки новых данных (в днях)', type=float, action='store')
    parser.add_argument('--debug', help='Enable debug mod', action='store_true', default=False)
    args = parser.parse_args()

    try:
        update_time = int(args.update_time * 24 * 60 * 60)

        while True:
            if args.gosat:
                pass


            if args.tansat:
                pass


            if args.oco2:
                pass
            
            time.sleep(update_time)

    except:
        pass
    
    finally:
        pass

    




if __name__ == "__main__":
    main()