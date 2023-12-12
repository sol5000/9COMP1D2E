   #detect collisions
    for platform in platforms:
        #detect landing on platform
        if platform.colliderect(pc):
            if platform.top < pc.bottom:
                pc.bottom = platform.top
                v[1] = 0