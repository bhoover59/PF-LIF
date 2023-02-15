from vpython import *
#Web VPython 3.2

# Set up the scene
scene = canvas(background = color.white)

# Set up the balls
hydrogen = sphere(pos = vector(-2, 4, 0), radius = 0.35, color = color.white)
oxygen1 = sphere(pos = vector(-1, 5, 0), radius = 0.35, color = color.red)
nitrogen = sphere(pos = vector(0, 4, 0), radius = 0.35, color = color.blue)
oxygen2 = sphere(pos = vector(1, 5, 0), radius = 0.35, color = color.red)

# Set up the bonds
stick1 = cylinder(pos = hydrogen.pos, axis = oxygen1.pos - hydrogen.pos, radius = 0.1, color = vector(0.5,0.5,0.5))
stick2 = cylinder(pos = oxygen1.pos, axis = nitrogen.pos - oxygen1.pos, radius = 0.1, color = vector(0.5,0.5,0.5))
stick3 = cylinder(pos = nitrogen.pos, axis = oxygen2.pos - nitrogen.pos, radius = 0.1, color = vector(0.5,0.5,0.5))

# Set up the initial velocity and time
velocity = vector(0, -0.01, 0)
velocity_photon = vector(0.05, 0, 0)
start_arrow = stick2.pos.x

# Times for segements
intercept_355 = 100
intercept_308 = 300
photon_time = 500
stop_time = 750

#scene.camera.follow(stick1) # follow OH molecule
scene.camera.pos = vector(0, 0, 15) # shift camera so you can see HONO move
t = 0
while t <= stop_time:
    rate(100)
    if (t < intercept_355):
        # Update the position of each ball
        hydrogen.pos += velocity
        nitrogen.pos += velocity
        oxygen1.pos += velocity
        oxygen2.pos += velocity
        stick1.pos = hydrogen.pos
        stick1.axis = oxygen1.pos - hydrogen.pos
        stick2.pos = oxygen1.pos
        stick2.axis = nitrogen.pos - oxygen1.pos
        stick3.pos = nitrogen.pos
        stick3.axis = oxygen2.pos - nitrogen.pos
    if (t >= intercept_355 &  t < intercept_308):
        # Move hydrogen, stick1, and oxygen1 upwards and to the right at 45 degrees
        hydrogen.pos += velocity
        oxygen1.pos += velocity
        stick1.pos += velocity
        stick1.axis = oxygen1.pos - hydrogen.pos
        # Delete NO and stick
        stick2.visible = False
        nitrogen.visible = False
        oxygen2.visible = False
        stick3.visible = False
        # Create arrow 
        light_355 = cylinder(pos = vector(start_arrow, start_arrow - 3, 0), axis = vector(0, 10, 0), color = color.red, radius = 0.1)
        L_355 = label(pos = light_355.pos, text = '355 nm laser', xoffset = 5, yoffset = -15, space = 5, height = 16, border = 4, font = 'sans')
    if (t >= intercept_308 & t < photon_time):
        hydrogen.pos += velocity
        oxygen1.pos += velocity
        stick1.pos += velocity
        stick1.axis = oxygen1.pos - hydrogen.pos
        # Delete NO and stick
        stick2.visible = False
        nitrogen.visible = False
        oxygen2.visible = False
        stick3.visible = False
        light_355.visible = False
        L_355.visible = False
        light_308 = cylinder(pos = vector(start_arrow, start_arrow - 3, 0), axis = vector(0, 10, 0), color = color.orange, radius = 0.1)
        L_308 = label(pos = light_308.pos, text = '308 nm laser', xoffset = 5, yoffset = -15, space = 5, height = 16, border = 4, font = 'sans')
    if (t >= photon_time):
        stick2.visible = False
        nitrogen.visible = False
        oxygen2.visible = False
        stick3.visible = False
        light_355.visible = False
        L_355.visible = False
        light_308.visible = False
        L_308.visible = False
        if (t == photon_time):
            photon = sphere(pos = oxygen1.pos, radius = 0.35, color = color.yellow)
            detector_offset = photon.pos + vector(10,0,0)
        photon.pos += velocity_photon
        detector = box(pos = detector_offset, length = 2, height = 5, width = 2)
        detector_label = label(pos = detector.pos + vector(0, 2, 0), text = 'Photon counter', xoffset = 5, yoffset = 15, space = 5, height = 16, border = 4, font = 'sans')
        if (photon.pos.x > detector.pos.x):
            photon.visible = False
    t += 1
