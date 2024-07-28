"""
File: database_manager.py
Author: Steven "Kabbe" Karbjinsky
Description: ...

For more information, see: https://github.com/xKabbe/ascendify
"""
import sqlite3
from pathlib import Path

from pandas import DataFrame


class DatabaseManager:
    def __init__(self, db_dir: str = 'data/database', db_name: str = 'ascendify.db'):
        db_dir = Path(db_dir)
        db_dir.mkdir(parents=True, exist_ok=True)

        self.db_name = db_name
        self.db_path = db_dir / db_name
        self.conn = None
        self.cursor = None

        self.connect()

    def connect(self):
        self.conn = sqlite3.connect(self.db_path)
        self.cursor = self.conn.cursor()

    def disconnect(self):
        if self.conn:
            self.conn.close()

    def create_schema(self):
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS videos (
                id TEXT PRIMARY KEY,
                path TEXT NOT NULL,
                title TEXT,
                extension TEXT,
                upload_date DATETIME,
                duration INTEGER,
                height INTEGER,
                width INTEGER
            )
        ''')

        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS frames (
                id TEXT PRIMARY KEY,
                video_id TEXT NOT NULL,
                frame_seq INTEGER NOT NULL,
                timestamp DATETIME,
                FOREIGN KEY(video_id) REFERENCES videos(id) ON DELETE CASCADE
            )
        ''')

        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS pose_landmarks (
                id TEXT PRIMARY KEY,
                frame_id TEXT NOT NULL,
                keypoint_id INTEGER,
                x REAL,
                y REAL,
                z REAL,
                visibility REAL,
                FOREIGN KEY(frame_id) REFERENCES frames(id) ON DELETE CASCADE,
                UNIQUE (frame_id, keypoint_id)
            )
        ''')

        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS pose_world_landmarks (
                id TEXT PRIMARY KEY,
                frame_id TEXT NOT NULL,
                keypoint_id INTEGER,
                x REAL,
                y REAL,
                z REAL,
                visibility REAL,
                FOREIGN KEY(frame_id) REFERENCES frames(id) ON DELETE CASCADE,
                UNIQUE (frame_id, keypoint_id)
            )
        ''')

        self.cursor.execute('''CREATE INDEX IF NOT EXISTS idx_frames_video_id
            ON frames(video_id)
        ''')

        self.cursor.execute('''CREATE INDEX IF NOT EXISTS idx_pose_landmarks_frame_id
            ON pose_landmarks(frame_id)
        ''')

        self.cursor.execute('''CREATE INDEX IF NOT EXISTS idx_pose_world_landmarks_frame_id
            ON pose_world_landmarks(frame_id)
        ''')

        self.conn.commit()

    def insert(self, table: str, data: dict):
        """
        db_manager.insert(table='videos', data={'path': 'example/path',
                                                'title': 'Example Title.mp4',
                                                'upload_date': '2024-07-27',
                                                'duration': 855,
                                                'resolution': 'Example Resolution'})
        """
        if not data:
            raise ValueError('Empty data.')

        print(table)
        print(data)

        columns = ', '.join(data.keys())
        placeholders = ', '.join('?' * len(data))

        self.cursor.execute(f'''
            INSERT INTO {table} ({columns})
            VALUES ({placeholders})
        ''', tuple(data.values()))

        self.conn.commit()

        return self.cursor.lastrowid

    def bulk_insert(self, table: str, data: DataFrame):
        if data.empty:
            raise ValueError('Empty data.')

        data.to_sql(table, con=self.conn, if_exists='append', index=False)
        # self.cursor.execute()

    def update(self, table: str, data: dict, conditions: list[str]):
        """
        db_manager.update(table='videos',
                          data={'title': 'Example Title Updated.mp4',
                                'duration': 900},
                          conditions=['where resolution = \'Example Resolution\'',
                                      'and duration = 855'])
        """
        if not data:
            raise ValueError(f'Empty data.')

        set_clause = ', '.join(f'{key} = ?' for key in data.keys())
        conditions = ' '.join(conditions)
        if not conditions.lower().startswith('where'):
            raise ValueError('Conditions parameter must contain a "where" clause.')

        self.cursor.execute(f'''
            UPDATE {table} SET {set_clause} {conditions}
        ''', tuple(data.values()))

        self.conn.commit()

    def delete(self, table: str, conditions: list[str]):
        """
        db_manager.delete(table='videos', conditions=['where resolution = \'Example Resolution 10x\'',
                                                      'or duration = 900'])
        """
        conditions = ' '.join(conditions)
        if not conditions.lower().startswith('where'):
            raise ValueError('Conditions parameter must contain a "where" clause.')

        self.cursor.execute(f'''
            DELETE FROM {table} {conditions}
        ''')

        self.conn.commit()

    def select(self):
        pass
