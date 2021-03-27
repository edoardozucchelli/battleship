import random


DIMENSION = 3
SHIP_MAX = 3

SHIPS_1 = [
    (0, 2), (1, 0), (2, 1)
]

SHIPS_2 = [
    (2, 1), (2, 0), (1, 1)
]


def get_correct_inp(x_or_y):
    value = None

    while True:
        try:
            value = int(input(
                x_or_y + ": " + "INSERIRE UN NUMERO DA 0 A " + str(SHIP_MAX) + " "))
        except ValueError:
            print("Il valore deve essere un numero!")
            continue

        if value < 0:
            print("Il valore deve essere positivo!.")
            continue
        if value > SHIP_MAX:
            print("Il valore deve essere uguale o inferiore a " + str(SHIP_MAX))
            continue
        else:
            break

    return value


class Grid:
    def __init__(self, dimension):
        self.dimension = dimension
        self.grid = self.build()

    def build(self):
        e = []

        for x in range(self.dimension):
            e.append([])

            for y in range(self.dimension):
                e[x].append('E')
        return e

    def describe(self):
        a = []

        for i, x in enumerate(self.grid):
            a.append([])
            for y in x:
                if y in ('E', 'S'):
                    a[i].append('?')
                else:
                    a[i].append(y)

        for x in a:
            print(x)


class Ship:
    def __init__(self, ship_max):
        self.ship_max = ship_max
        self.all_ships = []


class Player:
    def __init__(self, name, is_cpu=False, grid=None, ship=None):
        self.name = name
        self.is_cpu = is_cpu
        self.score = 0

        self.grid = grid
        self.ship = ship


class Game:
    def __init__(self, player_1_name, player_2_name, dimension, ship_max):
        self.grid_1 = Grid(dimension=dimension)
        self.grid_2 = Grid(dimension=dimension)

        self.ship_1 = Ship(ship_max=ship_max)
        self.ship_2 = Ship(ship_max=ship_max)

        self.player_1 = Player(name=player_1_name,
                               grid=self.grid_1,
                               ship=self.ship_1)

        self.player_2 = Player(name=player_2_name,
                               grid=self.grid_2,
                               ship=self.ship_2)

        self.player_1.opponent = self.player_2
        self.player_2.opponent = self.player_1

    # def select_random_player(self):
    #     players = [self.player_1, self.player_2]
    #     first_player = random.choice(players)
    #
    #     return first_player

    def populate_ships(self):
        self.ship_1.all_ships = SHIPS_1

        self.ship_2.all_ships = SHIPS_2

    def populate_grid(self, ship, grid):
        for x in ship.all_ships:
            grid.grid[x[0]][x[1]] = 'S'
        return grid.grid

    def sink_ship(self, grid, choice):
        if grid.grid[choice[0]][choice[1]] == 'S':
            grid.grid[choice[0]][choice[1]] = 'X'
            print('COLPITO E AFFONDATO!')
            return True

        elif grid.grid[choice[0]][choice[1]] == 'X':
            print('GIÀ COLPITO!')
        else:
            grid.grid[choice[0]][choice[1]] = 'A'
            print('UN BUCO NELL ACQUA...')

        return False


def main():

    print('##################')
    print('#BATTAGLIA NAVALE#')
    print('##################')

    player_1 = input('Inserisci nome giocatore 1: ')
    player_2 = input('Inserisci nome giocatore 2: ')

    game = Game(player_1_name=player_1,
                player_2_name=player_2,
                dimension=DIMENSION,
                ship_max=SHIP_MAX)

    game.populate_ships()

    game.populate_grid(game.player_1.ship, game.player_1.grid)
    game.populate_grid(game.player_2.ship, game.player_2.grid)

    print('PARTITA COMINCIATA!')

    while True:

        # PLAYER 1 TURN

        print('------------------------')
        print(game.player_1.name, 'turn')
        print('------------------------')

        game.player_2.grid.describe()

        to_sink_x = get_correct_inp('X')
        to_sink_y = get_correct_inp('Y')

        to_sink = (to_sink_x, to_sink_y)
        print('MISSILE INVIATO:', to_sink)

        if game.sink_ship(game.player_2.grid, (to_sink_x, to_sink_y)):
            game.player_1.score += 1
            print('PUNTEGGIO', player_1, '=', game.player_1.score)

            if game.player_1.score == SHIP_MAX:
                print(game.player_1.name, 'WIN!!!')
                break

        game.player_2.grid.describe()

        # PLAYER 2 TURN

        print('------------------------')
        print(game.player_2.name, 'turn')
        print('------------------------')

        game.player_1.grid.describe()

        to_sink_x = get_correct_inp('X')
        to_sink_y = get_correct_inp('Y')

        to_sink = (to_sink_x, to_sink_y)
        print('MISSILE INVIATO:', to_sink)

        if game.sink_ship(game.player_1.grid, to_sink):
            game.player_2.score += 1
            print('PUNTEGGIO', player_2, '=', game.player_2.score)

            if game.player_2.score == SHIP_MAX:
                print(game.player_2.name, 'WIN!!!')
                break

        game.player_1.grid.describe()

    print('PARTITA TERMINATA')


if __name__ == '__main__':
    main()
