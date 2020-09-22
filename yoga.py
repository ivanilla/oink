import webbrowser

selection = None

def classes(location):
    locations = {
        'a' : 'https://firstascentclimbing.com/avondale/yoga-classes/',
        'u' : 'https://firstascentclimbing.com/uptown/yoga-classes/',
        'b' : 'https://firstascentclimbing.com/block-37/yoga-classes/',
        'h' : 'https://firstascentclimbing.com/humboldt-park/yoga-humboldt-park/',
    }

    global selection
    
    while selection is None:
        try:
            selection = input('\nWhich location?\n a = Avondale\n u = Uptown\n b = Block 37\n h = Humbolt\n all = All\n\n')
            if selection == 'all':
                for i in locations:
                    webbrowser.open_new_tab(locations[i])
            else:
                webbrowser.open_new_tab(locations[selection])
        except:
            print('That is not an option--Try again')
            selection = None

classes(selection)