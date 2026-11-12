import argparse
import sys

from simulador import padron


def main() -> None:
    p = argparse.ArgumentParser(prog="simulador")
    sub = p.add_subparsers(dest="orden", required=True)
    pp = sub.add_parser("padron", help="genera un padrón sintético en CSV")
    pp.add_argument("--alumnos", type=int, default=300)
    pp.add_argument("--semilla", type=int, default=1)
    args = p.parse_args()
    if args.orden == "padron":
        sys.stdout.write(padron.a_csv(padron.generar(args.alumnos, args.semilla)))


main()
