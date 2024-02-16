from Crypto.Protocol.KDF import PBKDF2
from Crypto.Util.Padding import unpad
from pydantic import validate_call
from typing import Any, Optional
from datetime import datetime
from Crypto.Cipher import AES
import base64
import httpx
import json

class Ditlep:
    VALIDATE_CONFIG = dict(arbitrary_types_allowed = True)

    @validate_call(config = VALIDATE_CONFIG)
    def __init__(
        self,
        iv: str,
        password: str,
        salt: str,
        dk_len: int,
        count: int
    ) -> None:
        self.decrypt_config: dict[str, str] = {
            "iv": iv,
            "password": password,
            "salt": salt,
            "dk_len": dk_len,
            "count": count
        }

        self.base_url = "https://www.ditlep.com"

    @validate_call(config = VALIDATE_CONFIG)
    def _decrypt_data(self, encrypted_data: Any) -> Any:
        iv = bytes.fromhex(self.decrypt_config["iv"])
        password = self.decrypt_config["password"].encode()
        salt = self.decrypt_config["salt"].encode()

        key = PBKDF2(
            password,
            salt,
            dkLen = self.decrypt_config["dk_len"],
            count = self.decrypt_config["count"]
        )

        cipher = AES.new(
            key,
            AES.MODE_CBC,
            iv
        )

        decrypted_data = unpad(
            cipher.decrypt(
                base64.b64decode(encrypted_data)
            ),
            AES.block_size
        )

        return json.loads(decrypted_data.decode())

    @validate_call(config = VALIDATE_CONFIG)
    def _fetch_api(self, path: str, params: dict = {}) -> Any:
        response = httpx.get(f"{self.base_url}{path}", params = params)
        encrypted_data = response.text
        decrypted_data = self._decrypt_data(encrypted_data)
        return decrypted_data

    @validate_call(config = VALIDATE_CONFIG)
    def get_alliance_chests(self, month: Optional[int] = None) -> dict:
        if not month:
            current_date = datetime.now()
            month = current_date.month

        params = { "month": month }

        data = self._fetch_api("/AllianceChest/Get", params)

        return data

    @validate_call(config = VALIDATE_CONFIG)
    def get_dragon_tv(self, month: Optional[int] = None) -> dict:
        if not month:
            current_date = datetime.now()
            month = current_date.month

        params = { "month": month }

        data = self._fetch_api("/DragonTv/Get", params)

        return data

    @validate_call(config = VALIDATE_CONFIG)
    def get_dragons(
        self,
        name_or_id: str | int = "",
        rarities: list[str] = [],
        elements: list[str] = [],
        page_number: int = 0,
        page_size: int = 20,
        category: int | str = "",
        in_store: Optional[bool] = None,
        is_breedable: Optional[bool] = None,
        tag: str = ""
    ) -> dict:
        params = {
            "dragonName": name_or_id,
            "rarities": rarities,
            "elements": elements,
            "page": page_number,
            "pageSize": page_size,
            "category": category,
            "inStore": in_store,
            "breedable": is_breedable,
            "tag": tag
        }

        data = self._fetch_api("/Dragon/Search", params)

        return data

    @validate_call(config = VALIDATE_CONFIG)
    def get_items(
        self,
        id_or_name: str | int = "",
        sort: str = "",
        page_number: int | str = 1,
        page_size: int = 20,
        group: str = ""
    ) -> dict:
        params = {
            "sort": sort,
            "page": page_number,
            "pageSize": page_size,
            "group": group,
            "filter": f"TypeId~eq~'{id_or_name}'~or~Name~contains~'{id_or_name}'~or~BuildingTime~contains~'{id_or_name}'~or~Price~contains~'{id_or_name}'~or~Sell~contains~'{id_or_name}'~or~InStore~contains~'{id_or_name}'"
        }

        data = self._fetch_api("/Items/ItemFilter", params)

        return data

    @validate_call(config = VALIDATE_CONFIG)
    def get_breed_calculate_result(self, parent_ids: tuple[int, int]) -> dict:
        params = {
            "parent1Id": parent_ids[0],
            "parent2Id": parent_ids[1]
        }

        data = self._fetch_api("/Breeding/CalculateNewBreeding", params)

        return data

    def get_permanent_quests(self) -> dict:
        data = self._fetch_api("/Tournament/GetPermanentQuests")
        return data
    
    def get_temporary_quests(self) -> dict:
        data = self._fetch_api("/Tournament/GetAll")
        return data

    @validate_call(config = VALIDATE_CONFIG)
    def get_fog_islands(self, id: Optional[int] = None) -> dict:
        params = {}

        if not id is None:
            params["id"] = id

        data = self._fetch_api("/FogIsland/Get", params)

        return data

    @validate_call(config = VALIDATE_CONFIG)
    def get_grid_islands(self, id: Optional[int] = None) -> dict:
        params = {}

        if not id is None:
            params["id"] = id

        data = self._fetch_api("/GridIsland/Get", params)

        return data

    @validate_call(config = VALIDATE_CONFIG)
    def get_heroic_races(self, id: Optional[int] = None) -> dict:
        params = {}

        if not id is None:
            params["id"] = id

        data = self._fetch_api("/HeroicRace/Get", params)

        return data

    @validate_call(config = VALIDATE_CONFIG)
    def get_maze_islands(self, id: Optional[int] = None) -> dict:
        params = {}

        if not id is None:
            params["id"] = id

        data = self._fetch_api("/MazeIsland/Get", params)

        return data

    @validate_call(config = VALIDATE_CONFIG)
    def get_puzzle_islands(self, id: Optional[int] = None) -> dict:
        params = {}

        if not id is None:
            params["id"] = id

        data = self._fetch_api("/PuzzleIsland/Get", params)

        return data

    @validate_call(config = VALIDATE_CONFIG)
    def get_runner_islands(self, id: Optional[int] = None) -> dict:
        params = {}

        if not id is None:
            params["id"] = id

        data = self._fetch_api("/RunnerIsland/Get", params)

        return data

    @validate_call(config = VALIDATE_CONFIG)
    def get_tower_islands(self, id: Optional[int] = None) -> dict:
        params = {}

        if not id is None:
            params["id"] = id

        data = self._fetch_api("/TowerIsland/Get", params)

        return data