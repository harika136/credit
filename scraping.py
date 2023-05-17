import requests
from bs4 import BeautifulSoup
import csv

def scrape_credit_cards():
    url = "https://www.hdfcbank.com/personal/pay/cards/credit-cards"

    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")

    cards = []

    card_elements = soup.select(".credit-cards .credit-card-wrapper")
    for card_element in card_elements:
        card_name = card_element.select_one(".credit-card-name").text.strip()
        card_fee = card_element.select_one(".card-fee").text.strip()
        reward_points = card_element.select_one(".reward-points").text.strip()
        lounge_access = card_element.select_one(".lounge-access").text.strip()
        milestone_benefit = card_element.select_one(".milestone-benefit").text.strip()
        card_fee_reversal = card_element.select_one(".card-fee-reversal").text.strip()

        cards.append([card_name, card_fee, reward_points, lounge_access, milestone_benefit, card_fee_reversal])

    return cards

def export_to_csv(cards):
    with open("credit_cards.csv", "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["Card Name", "Card Fee", "Reward Points", "Lounge Access", "Milestone Benefit", "Card Fee Reversal"])
        writer.writerows(cards)

if __name__ == "__main__":
    credit_cards = scrape_credit_cards()
    export_to_csv(credit_cards)
    print("Data scraped and exported to credit_cards.csv")
