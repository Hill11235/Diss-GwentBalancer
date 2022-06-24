from gwent.cards.card import Card


class UnitCard(Card):

    def get_row(self):
        if self.agile:
            return [0, 1]
        return [self.row]

    def place_card(self, board, player, opponent, opponent_board, row, target):
        self.row = row
        player.remove_card_from_hand(self.card_id)
        board.rows[self.row].append(self)
        self.battlecry(board, player, opponent, opponent_board, row, target)

    def battlecry(self, board, player, opponent, opponent_board, row, target):
        # calls any abilities when a card is played, overridden in subclasses
        pass

    def get_active_strength(self, board):
        horn_buff = self.get_horn_buff(board)
        morale_buff = self.get_morale_buff(board)
        horn_buff = horn_buff / 2 if self.horn else horn_buff

        if self.hero:
            return self.strength
        elif any(card.weather for card in board.rows[self.row]):
            return (1 + morale_buff) * horn_buff
        else:
            return (self.strength + morale_buff) * horn_buff

    def get_horn_buff(self, board):
        horn = 1

        for card in board.rows[self.row]:
            if card.horn or card.horn_special:
                horn *= 2

        return horn

    def get_morale_buff(self, board):
        morale = -1 if self.morale_boost else 0

        for card in board.rows[self.row]:
            if card.morale_boost:
                morale += 1
        return morale

    def get_current_status(self, board=None):
        current_status = {
            "name": self.name,
            "faction": self.faction,
            "row": self.get_row(),
            "strength": self.strength,
            "hero": self.hero
        }
        if board is not None:
            current_status["active_strength"] = self.get_active_strength(board)

        return current_status
