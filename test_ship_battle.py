from ship_battle import Player, Grid, Ship, Game


class TestShipBattle:

    def test_grid(self):
        grid = Grid(dimension=3)

        assert grid

        test_grid = [
            ['E', 'E', 'E'],
            ['E', 'E', 'E'],
            ['E', 'E', 'E'],
        ]

        assert grid.grid == test_grid

        test_grid = [
            ['S', 'A', 'E'],
            ['E', 'E', 'E'],
            ['E', 'S', 'S'],
        ]

        grid.grid = test_grid
        grid.describe()

    def test_ship(self):
        ship = Ship(ship_max=4)

        assert ship
        assert ship.ship_max == 4
        assert ship.all_ships == []

    def test_player(self):
        player_1 = Player(name='player_1')

        assert player_1
        assert player_1.name == 'player_1'
        assert player_1.is_cpu is False
        assert player_1.score == 0

        assert player_1.grid is None
        assert player_1.ship is None

        assert player_1.opponent is None

        player_2 = Player(name='player_2', is_cpu=True)

        assert player_2.is_cpu is True

    def test_game(self):
        player_1_name = 'player_1'
        player_2_name = 'player_2'

        game = Game(player_1_name=player_1_name,
                    player_2_name=player_2_name,
                    dimension=3,
                    ship_max=4)

        assert game

        game.ship_1.all_ships = [(0, 0), (1, 2)]

        population = [
            ['S', 'E', 'E'],
            ['E', 'E', 'S'],
            ['E', 'E', 'E']
        ]

        assert game.populate_grid(
            ship=game.ship_1,
            grid=game.grid_1) == population

        sink_ship_x = [
            ['X', 'E', 'E'],
            ['E', 'E', 'S'],
            ['E', 'E', 'E']
        ]

        game.sink_ship(
            grid=game.grid_1,
            choice=(0, 0))

        assert game.grid_1.grid == sink_ship_x

        sink_ship_a = [
            ['X', 'A', 'E'],
            ['E', 'E', 'S'],
            ['E', 'E', 'E']
        ]

        game.sink_ship(
            grid=game.grid_1,
            choice=(0, 1))\

        assert game.grid_1.grid == sink_ship_a
