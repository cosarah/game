import argparse
import streamlit as st
import json


def print_text(s):
        i = 0
        while i+40 <= len(s):
            st.markdown(s[i:i+40])
            i += 40
        st.markdown(s[i:-1])


class Game:

    def __init__(self):
        parser = argparse.ArgumentParser(description='Begin a game')
        parser.add_argument('article', type=str, default='game_01',
                            help='Select an article,[game_01, game_02]')
        parser.add_argument('--path', type=str, default='', help="Enter the path of your article")

        args = parser.parse_args()
        if args.path == '':
            with open(f'{args.article}.json', 'r', encoding="utf-8") as art:
                self.data = json.loads(art.read())
        else:
            with open(args.path, 'r', encoding='utf-8') as art:
                self.data = json.loads(art.read())

        self.answer = []
        self.l = len(self.data["question"])

    def make(self):
        st.markdown('填词游戏')
        if self.data["title"]:
            st.title(self.data["title"])
        if self.data["description"]:
            st.markdown(self.data["description"])

        for i in range(self.l-1):
            ans = st.text_input(f"{i+1}.", self.data["answer"][i])
            self.answer.append(ans)

    def show(self):
        qa = ['**=='+self.answer[i // 2]+'==**' if i % 2 else self.data["question"][i // 2] for i in range(self.l * 2 - 1)]
        content = ''.join(qa)
        print_text(content)


game = Game()
game.make()
btn = st.button(':blue[Show the article]')
if btn:
    game.show()


