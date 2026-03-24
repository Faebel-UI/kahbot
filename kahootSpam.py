import asyncio
from multiprocessing import Process
from kahoot import KahootClient
from kahoot.packets.server.question_start import QuestionStartPacket
from os import system
from time import sleep


def spam(repeat):
    if repeat:
        OFFSET = 0
        while True:
            threads = []
            for i in range(OFFSET + 1, AMOUNT + OFFSET + 1):
                t = Process(target=lambda: asyncio.run(run(i)))
                t.start()
                threads.append(t)
                print(f"[+] Bot #{i} joining...")
                sleep(0.1)

            print("---------------------------------------")
            print("[!] All bots have joined, restarting...")
            print("---------------------------------------")

            for t in threads:
                t.kill()
            OFFSET += AMOUNT

    else:
        for i in range(1, AMOUNT + 1):
            t = Process(target=lambda: asyncio.run(run(i)))
            t.start()
            print(f"[+] Bot #{i} joining...")


def manual():
    global PIN, AMOUNT, PREFIX
    PIN = int(input("[!] Game PIN: "))
    AMOUNT = int(input("[!] Bot Amount (max. 245): "))
    PREFIX = input("[!] Prefix: ")
    system("clear")

    spam(False)


def auto():
    global PIN, AMOUNT, PREFIX
    PIN = int(input("[!] Game PIN: "))
    AMOUNT = 200
    PREFIX = input("[!] Prefix: ")
    system("clear")

    spam(True)


async def question_start(packet: QuestionStartPacket):
    print(f"Question started: {packet}")


async def run(id):
    client = KahootClient()
    client.on("question_start", question_start)
    await client.join_game(game_pin=PIN, username=f"{PREFIX}{id}")


def main():
    print("---------------------------------------")
    print("             Kahoot Spammer")
    print("---------------------------------------\n")
    MODE = int(input("[1] Manual\n[2] Auto\n--> "))
    print()
    if MODE == 1:
        manual()
    elif MODE == 2:
        auto()
