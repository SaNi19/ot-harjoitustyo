

class MovePlayer:
    """Luokka, jonka avulla siirretään pelihahmoa ja palloja.
    """

    def __init__(self, map, height, width, step, move_y, move_x, find, game_end):
        """Luokan konstruktori, joka luo pelihahmolle ja pallolle uuden sijainnin.

        Attributes:
            map: Pelitaulukko.
            height: Pelitaulukon korkeus.
            width: Pelitaulukon leveys.
            step: Pelin askel-muuttuja.
            move_y: Pelihahmon siirtymän y-arvo.
            move_x: Pelihahmon siirtymän x-arvo.
            find: Metodi, joka palauttaa pelihahmon sijainnin.
            game_end: Metodi, joka palauttaa True, jos kaikki pallot on varastossa, muuten False.

        """


        self.map = map
        self.height = height
        self.width = width
        self.step = step
        self.move_y = move_y
        self.move_x = move_x
        self.find = find
        self.game_end = game_end

    def move(self, move_y, move_x):
        """Metodi, joka asettaa pelihahmon ja pallon x- ja y-arvot.

        Args:
            move_y: Siirtymä x-akselilla.
            move_x: Siirtymä y-akselilla.
        """
        wall = 1
        ball = 3
        end = 5
        """Pelilaudan numerointia vastaavat nimet.
        """

        """Tarkistaa onko kaikki pallot varastossa.
        """
        if self.game_end():
            return

        """Esii pelihahmon sijainnin ja antaa pelihahmolle uude x- ja y-arvot.
        """

        old_player_y, old_player_x = self.find()
        new_player_y = old_player_y + move_y
        new_player_x = old_player_x + move_x

        """Tarkistaa onko pelihahmon siirtymäsuunnassa seinä.
        """

        if self.map[new_player_y][new_player_x] == wall:
            return

        """Jos pelihamo voi liikkua, asettaa palolle uudet x- ja y-arvot.
        """

        if self.map[new_player_y][new_player_x] in [ball, end]:
            new_ball_y = new_player_y + move_y
            new_ball_x = new_player_x + move_x

            """Tarkistaa onko pallo varastossa.
            """

            if self.map[new_ball_y][new_ball_x] in [wall, ball, end]:
                return

            """Asettaa pelihamolle ja palolle uudet x- ja y-arvot
            """

            self.map[new_player_y][new_player_x] -= 3
            self.map[new_ball_y][new_ball_x] += 3

        """Siirtää pelihamon pelilaudalla uuteen sijaintiin ja lisää askeleen.
        """

        self.map[old_player_y][old_player_x] -= 4
        self.map[new_player_y][new_player_x] += 4
        self.step += 1
