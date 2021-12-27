import main
import random

def test_end_to_end_OK():
    # Create a new entry
    random_number = str(random.randint(0, 100))
    entry_json = {
        "name": "automated_name" + random_number,
        "description": "Random description " + random_number
    }
    entry = main.create_entry(entry_json)
    entry_id = entry.json()['_id']
    print("Created entry with id " + entry_id)

    # Check that it was created and that exist on the db
    found_entry = main.get_one(entry_id).json()
    assert found_entry['name'] == entry_json['name']
    assert found_entry['description'] == entry_json['description']
    print("The entry with the id " + entry_id + " has been created successfully")
    #assert entries[-1] == entry_json
    #print(entries[-1]['name'])

    # Modify current entry
    random_number = str(random.randint(0, 100))
    entry_json = {
        "name": "new_automated_name" + random_number,
        "description": "New random description " + random_number
    }
    main.update_entry(entry_id, entry_json)

    # Check the changes had effect
    found_entry = main.get_one(entry_id).json()
    assert found_entry['name'] == entry_json['name']
    assert found_entry['description'] == entry_json['description']
    print("The entry with the id " + entry_id + " has been modified successfully")

    # Delete Entry
    main.delete_entry(entry_id)

    # Check that it was deleted
    found_entry = main.get_one(entry_id).json()
    assert found_entry['title'] == 'Not Found'
    print("The entry with the id " + entry_id + " has been deleted successfully")

def test_show_all_entries():
    # Search for all entries and get the number of entries
    entries = main.get_all_entries()
    number_of_entries = len(entries.json())
    print("Got the number of entries before creating a new one")
    
    # Create a new entry
    random_number = str(random.randint(0, 100))
    entry_json = {
        "name": "automated_name" + random_number,
        "description": "Random description " + random_number
    }
    main.create_entry(entry_json)
    print("New entry has been created successfully")

    # Search again for all entries
    entries = main.get_all_entries()

    # Check that the number of entries had increased
    curr_number_of_entries = len(entries.json())
    assert curr_number_of_entries == number_of_entries + 1
    print("The 'get' api got all the entries, including the new one")

def test_get_entry_with_wrong_id():
    # Search for an non existing entry
    fake_entry = main.get_one('14')

    # Check that is giving a 404 error
    assert fake_entry.status_code == 404
    print("The api call is returning 404 not found when searching for a non existing entry")

def test_update_non_existing_entry():
    # Try to modify a non existing entry
    fake_entry_json = {
        "name": "name",
        "description": "description"
    }
    fake_entry = main.update_entry('14', fake_entry_json)

    # Check that is giving a 404 error
    assert fake_entry.status_code == 404
    print("The api call is returning 404 not found when searching for a non existing entry to update")

def test_delete_non_existing_entry():
    # Try to delete a non existing entry
    fake_entry = main.delete_entry('14')
    
    # Check that is giving a 404 error
    assert fake_entry.status_code == 404
    print("The api call is returning 404 not found when searching for a non existing entry to delete")
    # intentar borrar una entrada que no existe