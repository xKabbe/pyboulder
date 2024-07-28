"""
File: setup_database_schema.py
Author: Steven "Kabbe" Karbjinsky
Description: ...

For more information, see: https://github.com/xKabbe/ascendify
"""
from api.utils.classes.database_manager import DatabaseManager


def main():
    db_manager = DatabaseManager()
    db_manager.create_schema()


if __name__ == '__main__':
    main()
