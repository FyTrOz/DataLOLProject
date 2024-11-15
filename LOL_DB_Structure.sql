CREATE TABLE "Players" (
  "puuid" integer PRIMARY KEY,
  "player_name" varchar,
  "gameName" varchar,
  "tagLine" varchar
);

CREATE TABLE "Game_Player" (
  "puuid" integer,
  "new_match_id" integer,
  "summoner_name" varchar,
  "summoner_id" varchar,
  "summoner_level" int,
  "champion_name" varchar,
  "kills" int,
  "deaths" int,
  "assists" int,
  "total_damage_dealt" int,
  "total_damage_taken" int,
  "total_heal" int,
  "gold_earned" int,
  "vision_score" int,
  "win" bool,
  PRIMARY KEY ("puuid", "new_match_id")
);

CREATE TABLE "Games" (
  "new_match_id" integer PRIMARY KEY,
  "game_number" integer,
  "game_date" date,
  "result" varchar
);

CREATE TABLE "Match_Info" (
  "new_match_id" integer PRIMARY KEY,
  "end_of_game_result" varchar,
  "game_creation" bigint,
  "game_duration" int,
  "game_end_timestamp" bigint,
  "game_mode" varchar,
  "game_name" varchar,
  "game_start_timestamp" bigint,
  "game_type" varchar,
  "game_version" varchar,
  "map_id" int
);

ALTER TABLE "Players" ADD FOREIGN KEY ("puuid") REFERENCES "Game_Player" ("puuid");

ALTER TABLE "Games" ADD FOREIGN KEY ("new_match_id") REFERENCES "Game_Player" ("new_match_id");

ALTER TABLE "Game_Player" ADD FOREIGN KEY ("new_match_id") REFERENCES "Match_Info" ("new_match_id");
