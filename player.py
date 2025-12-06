import pygame
from circleshape import CircleShape
from constants import PLAYER_RADIUS, LINE_WIDTH, PLAYER_TURN_SPEED, PLAYER_SPEED, PLAYER_SHOOT_SPEED, SHOT_RADIUS, PLAYER_SHOOT_COOLDOWN_SECONDS
from shot import Shot

class Player(CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, PLAYER_RADIUS)
        self.rotation = 0
        self.shot_cooldown = 0 #timer for cooldown start with a value of 0

    # in the Player class
    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]

    def rotate(self, dt):
        self.rotation = self.rotation + (PLAYER_TURN_SPEED * dt)

    def update(self, dt):
        if self.shot_cooldown > 0:
            self.shot_cooldown -= dt
            if self.shot_cooldown < 0:
                self.shoot_cooldown = 0

        keys = pygame.key.get_pressed()

        if keys[pygame.K_a]:
            self.rotate(-dt)
        if keys[pygame.K_d]:
            self.rotate(dt)
        if keys[pygame.K_w]:
            self.move(dt)
        if keys[pygame.K_s]:
            self.move(-dt)
        if keys[pygame.K_SPACE]:
            self.shoot()
    
    def draw(self, screen):
        list_point = self.triangle()
        pygame.draw.polygon(screen, "white", list_point, LINE_WIDTH)

    def move(self, dt):
        unit_vector = pygame.Vector2(0, 1)
        rotated_vector = unit_vector.rotate(self.rotation)
        rotated_with_speed_vector = rotated_vector * PLAYER_SPEED * dt
        self.position += rotated_with_speed_vector

    def shoot(self):
        # 1. Check if we are still cooling down
        if self.shot_cooldown > 0:
            return # too soon, do nothing

        # 2. Start cooldown
        self.shot_cooldown = PLAYER_SHOOT_COOLDOWN_SECONDS

        # 3. Actually create and fire the shoot
        # 3.1. Create the new shot (bullet) at the player's current position
        new_shot = Shot(self.position.x, self.position.y, SHOT_RADIUS)
        
        # 3.2. Figure out the bullet's direction and speed (velocity)
        base_direction = pygame.Vector2(0, 1)
        rotated_direction = base_direction.rotate(self.rotation)
        final_velocity_vector = rotated_direction * PLAYER_SHOOT_SPEED

        # 3.3. Tell the new shot to use this calculated velocity
        new_shot.velocity = final_velocity_vector



        # Alternative implementation
        # 1. Create the new Shot (bullet) at the player's current position
        # > new_shot = Shot(self.position.x, self.position.y, SHOT_RADIUS)

        # 2. Assign the final calculated velocity to the new_shot
        #    This single does what three lines did previously:
        #       - Starts with pygame.Vector2(0, 1)
        #       - Rotate it by self.rotation
        #       - Multiples the result by PLAYER_SHOOT_SPEED
        # > new_shot.velocity = pygame.Vector2(0, 1).rotate(self.rotation) * PLAYER_SHOOT_SPEED
        # my mistakes here
        # > Shot.velocity = pygame.Vector2(0, 1) pygame.Vector2.rotate(self.rotation + 0) * PLAYER_SHOOT_SPEED

        
