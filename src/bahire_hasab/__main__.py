#!/usr/bin/env python3

from tabulate import tabulate
import datetime
import argparse
from bahire_hasab import BahireHasab
import logging 



def main():
    parser = argparse.ArgumentParser(
        description="Prints the dates of lents and holidays in a year for Ethiopian Calendar.",
        formatter_class=argparse.MetavarTypeHelpFormatter,
    )
    parser.add_argument(
        "Year",
        default=None,
        type=int,
        help="Assings the year for the table",
        nargs="?",
    )
    parser.add_argument(
        "-a",
        "--all",
        help="Prints the table of lents and holidays in a year",
        action="store_true",
    )
    parser.add_argument(
        "-n",
        "--new-year",
        help="Prints the day of the new year in Ethiopia Calendar.",
        action="store_true",
    )
    parser.add_argument(
        "-tn",
        "--tsome-neneweh",
        help="Prints the day of Tsome neneweh in Ethiopia Calendar.",
        action="store_true",
    )
    parser.add_argument(
        "-ats",
        "--abiy-tsome",
        help="Prints the day of the Abiy Tsome in Ethiopia Calendar.",
        action="store_true",
    )
    parser.add_argument(
        "-dz",
        "--debre-zeyt",
        help="Prints the day of Debre Zeyt  in Ethiopia Calendar.",
        action="store_true",
    )
    parser.add_argument(
        "-hs",
        "--hosaena",
        help="Prints the day of Hosaena in Ethiopia Calendar.",
        action="store_true",
    )
    parser.add_argument(
        "-sk",
        "--siklet",
        help="Prints the day of HolyFriday in Ethiopia Calendar.",
        action="store_true",
    )
    parser.add_argument(
        "-f",
        "--fasika",
        help="Prints the day of the Easter in Ethiopia Calendar.",
        action="store_true",
    )
    parser.add_argument(
        "-er",
        "--erget",
        help="Prints the date of erget",
        action="store_true",
    )
    parser.add_argument(
        "-bh",
        "--beale_hamsa",
        help="Prints the day of Pentecost in Ethiopia Calendar.",
        action="store_true",
    )
    parser.add_argument(
        "-th",
        "--tsome-hawaryat",
        help="Prints the day of Tsome Hawaryat in Ethiopia Calendar.",
        action="store_true",
    )
    parser.add_argument(
        "-td",
        "--tsome-dhnet",
        help="Prints the day of Tsome Dhnet in Ethiopia Calendar.",
        action="store_true",
    )
    parser.add_argument(
        '-l',
        '--log-level',
        help="Loglever setter for the cli.",
        choices=['debug', 'info', 'warning', 'error', 'critical'],
        default='info'
    )
    args: argparse.Namespace = parser.parse_args()

    log_level = args.log_level.upper()
    
    logging.basicConfig(format='%(asctime)s | %(funcName)s | %(message)s ', datefmt='%d-%b-%y %H:%M:%S', level=log_level)

    logger = logging.getLogger(__name__)
    # --------------------------------------------
    if args.Year == None:
        year = BahireHasab(datetime.datetime.now().year - 8)
    else:
        try:
            year = BahireHasab(args.Year, logger=logger)
        except:
            logging.exception(f"{args.Year} caused an Error please try again by using integer.")
    arguments = [
        "new_year",
        "tsome_neneweh",
        "abiy_tsome",
        "debre_zeyt",
        "hosaena",
        "siklet",
        "fasika",
        "erget",
        "beale_hamsa",
        "tsome_hawaryat",
        "tsome_dhnet",
    ]
    methods = [
        "new_year",
        "neneweh",
        "abiy_tsom",
        "debre_zeyt",
        "hosaena",
        "sklet",
        "tnsae",
        "erget",
        "beale_hamsa",
        "tsome_hawaryat",
        "tsome_dhnet",
    ]
    heading = ["በዓለት", "የሚውሉበት ቀን"]
    name = [
        "ዓመተ ምህረት፡",
        "ወንጌላዊ፡",
        "እንቁጣጣሽ፡",
        "ጾመ ነነዌ፡",
        "ዓቢይ ጾም፡",
        "ደብረ ዘይት፡",
        "ሆሳዕና፡",
        "ስቅለት፡",
        "ትንሳኤ፡",
        "እርገት፡",
        "ጰራቅሊጦስ፡",
        "ጾመ ሐዋርያት፡",
        "ጾመ ድኅነት፡",
    ]
    value = [
        args.Year,
        year.wengelawi,
        year.new_year,
        year.neneweh,
        year.abiy_tsom,
        year.debre_zeyt,
        year.hosaena,
        year.sklet,
        year.tnsae,
        year.erget,
        year.beale_hamsa,
        year.tsome_hawaryat,
        year.tsome_dhnet,
    ]
    table = zip(name, value)
    # --------------------------------------------
    if args.all:
        logger.debug('showing table')
        print(tabulate(table, headers=heading,tablefmt="simple_grid"));
 
    for a, m in zip(arguments, methods):
        if getattr(args, a):
            print(getattr(year, m))


if __name__ == "__main__":
    main()
