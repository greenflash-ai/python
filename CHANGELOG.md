# Changelog

## 1.1.0 (2026-01-30)

Full Changelog: [v1.0.1...v1.1.0](https://github.com/greenflash-ai/python/compare/v1.0.1...v1.1.0)

### Features

* **client:** add custom JSON encoder for extended type support ([a20ec3b](https://github.com/greenflash-ai/python/commit/a20ec3bfef1c80fcf8c1fd6cfc2d4c86feedcba5))

## 1.0.1 (2026-01-24)

Full Changelog: [v1.0.0...v1.0.1](https://github.com/greenflash-ai/python/compare/v1.0.0...v1.0.1)

### Chores

* **ci:** upgrade `actions/github-script` ([2226275](https://github.com/greenflash-ai/python/commit/2226275ae3567b06028c60f45085548f781f0430))

## 1.0.0 (2026-01-21)

Full Changelog: [v0.40.0...v1.0.0](https://github.com/greenflash-ai/python/compare/v0.40.0...v1.0.0)

### Chores

* **internal:** update `actions/checkout` version ([db4caee](https://github.com/greenflash-ai/python/commit/db4caeed0cf6a01376a2d7e4f2e0e789ec68ccd0))

## 0.40.0 (2026-01-14)

Full Changelog: [v0.1.0-alpha.27...v0.40.0](https://github.com/greenflash-ai/python/compare/v0.1.0-alpha.27...v0.40.0)

### Features

* **api:** manual updates ([7137d99](https://github.com/greenflash-ai/python/commit/7137d99beba8c434ea41fb1c83b6c4f49bf80d4b))
* **client:** add support for binary request streaming ([b9397f0](https://github.com/greenflash-ai/python/commit/b9397f0e24f7736a0f563fd9cc8d63d70b3a41c3))


### Bug Fixes

* **client:** loosen auth header validation ([18728a4](https://github.com/greenflash-ai/python/commit/18728a4f607e510a513d4ceee3c20201d1b4ee61))
* ensure streams are always closed ([d502131](https://github.com/greenflash-ai/python/commit/d502131b52e35f71673362c6ece423fda17cc949))
* **types:** allow pyright to infer TypedDict types within SequenceNotStr ([179acea](https://github.com/greenflash-ai/python/commit/179aceae90318e6d54665dea6bf9463950f170da))
* use async_to_httpx_files in patch method ([1f0e917](https://github.com/greenflash-ai/python/commit/1f0e91728bff46f4d6725ea4cb921de107f96840))


### Chores

* add missing docstrings ([e5701df](https://github.com/greenflash-ai/python/commit/e5701df6d98991cdc05474d4f345da01b9132d1b))
* **deps:** mypy 1.18.1 has a regression, pin to 1.17 ([9eebcd1](https://github.com/greenflash-ai/python/commit/9eebcd1a77913a84c5ede342d222e8a801afc0ee))
* **docs:** use environment variables for authentication in code snippets ([2f7d590](https://github.com/greenflash-ai/python/commit/2f7d590f5be07f293c8f1a07af3c90440de3d973))
* **internal:** add `--fix` argument to lint script ([0a0dbd2](https://github.com/greenflash-ai/python/commit/0a0dbd2333bef4dff767b0ec07300fd127f3e63f))
* **internal:** add missing files argument to base client ([1c45f5f](https://github.com/greenflash-ai/python/commit/1c45f5fcd739bcfd5c6b4492713331547b26cab6))
* **internal:** codegen related update ([626cd83](https://github.com/greenflash-ai/python/commit/626cd83e4b8f37a17eb7744930f9705371b82152))
* **internal:** codegen related update ([58976f2](https://github.com/greenflash-ai/python/commit/58976f26865e13f3539654a79c56f39fe57bc541))
* speedup initial import ([b313fdc](https://github.com/greenflash-ai/python/commit/b313fdc679b3f77c04c1e2751201fa22f15c991d))
* update lockfile ([d4e41dc](https://github.com/greenflash-ai/python/commit/d4e41dc28433659c1dd29a77add4453f046bd1f7))

## 0.1.0-alpha.27 (2025-11-24)

Full Changelog: [v0.1.0-alpha.26...v0.1.0-alpha.27](https://github.com/greenflash-ai/python/compare/v0.1.0-alpha.26...v0.1.0-alpha.27)

### Features

* **api:** manual updates ([7ec0d67](https://github.com/greenflash-ai/python/commit/7ec0d67da52350b0662c9af3bb75ad1b4b7604c8))


### Bug Fixes

* **client:** close streams without requiring full consumption ([bcef392](https://github.com/greenflash-ai/python/commit/bcef392890431c33b64e1cf98656d9a1f03e073c))
* compat with Python 3.14 ([5988545](https://github.com/greenflash-ai/python/commit/59885458a02d0c518bc262dcd95db393bffae805))
* **compat:** update signatures of `model_dump` and `model_dump_json` for Pydantic v1 ([e22d13c](https://github.com/greenflash-ai/python/commit/e22d13cae512062d3ae037bd3d1a36de727c0d03))


### Chores

* add Python 3.14 classifier and testing ([0eeb499](https://github.com/greenflash-ai/python/commit/0eeb499fc63e9c24bb7db173652976cbe7f688cb))
* **internal/tests:** avoid race condition with implicit client cleanup ([9137f05](https://github.com/greenflash-ai/python/commit/9137f05ecf1e21b2c1bf33a62f868fea0915b514))
* **internal:** grammar fix (it's -&gt; its) ([f63f785](https://github.com/greenflash-ai/python/commit/f63f7855532fa93ee4e353bb4c9d9aeacf196925))
* **package:** drop Python 3.8 support ([b74fd7d](https://github.com/greenflash-ai/python/commit/b74fd7d22aef73f1d36907eb938508c7d3bab396))

## 0.1.0-alpha.26 (2025-10-29)

Full Changelog: [v0.1.0-alpha.25...v0.1.0-alpha.26](https://github.com/greenflash-ai/python/compare/v0.1.0-alpha.25...v0.1.0-alpha.26)

### Features

* **api:** manual updates ([35290cf](https://github.com/greenflash-ai/python/commit/35290cf68491b7ac16db13b074a1504a64164f3a))


### Chores

* bump `httpx-aiohttp` version to 0.1.9 ([f7e8be0](https://github.com/greenflash-ai/python/commit/f7e8be0ab7952f0c34f98daaee1190584ab2d3d9))
* **internal:** detect missing future annotations with ruff ([91eee0f](https://github.com/greenflash-ai/python/commit/91eee0f2b86d6e7369f9a485ee4bb07af113f101))

## 0.1.0-alpha.25 (2025-10-09)

Full Changelog: [v0.1.0-alpha.24...v0.1.0-alpha.25](https://github.com/greenflash-ai/python/compare/v0.1.0-alpha.24...v0.1.0-alpha.25)

### Features

* **api:** manual updates ([828f579](https://github.com/greenflash-ai/python/commit/828f5795403516c6ea026d2e1e32aaa02afdae54))
* **api:** manual updates ([4c42120](https://github.com/greenflash-ai/python/commit/4c4212091c37b75d72ae953bc878ff438bfa01fc))


### Chores

* remove custom code ([c75b03f](https://github.com/greenflash-ai/python/commit/c75b03fb934c8bbacea925063a70c2a2c165a928))

## 0.1.0-alpha.24 (2025-09-27)

Full Changelog: [v0.1.0-alpha.23...v0.1.0-alpha.24](https://github.com/greenflash-ai/python/compare/v0.1.0-alpha.23...v0.1.0-alpha.24)

### Features

* **api:** add organization endpoint ([2af098e](https://github.com/greenflash-ai/python/commit/2af098e976a5f23634491745c351e158da196b3f))
* **api:** add organizations and examples to config ([5cc1517](https://github.com/greenflash-ai/python/commit/5cc15177f0a7dfa7ddfbe7901edfb7f54fe72efc))
* **api:** organization to organizations ([74a91af](https://github.com/greenflash-ai/python/commit/74a91af2f510a7ce9f5dce7252954d537af27d07))

## 0.1.0-alpha.23 (2025-09-22)

Full Changelog: [v0.1.0-alpha.22...v0.1.0-alpha.23](https://github.com/greenflash-ai/python/compare/v0.1.0-alpha.22...v0.1.0-alpha.23)

### Features

* **api:** manual updates ([0513015](https://github.com/greenflash-ai/python/commit/0513015c03a5d780f305cbec2176918b61e96df3))

## 0.1.0-alpha.22 (2025-09-20)

Full Changelog: [v0.1.0-alpha.21...v0.1.0-alpha.22](https://github.com/greenflash-ai/python/compare/v0.1.0-alpha.21...v0.1.0-alpha.22)

### Chores

* do not install brew dependencies in ./scripts/bootstrap by default ([3daae6d](https://github.com/greenflash-ai/python/commit/3daae6d028f4efcc15379680ebed11facc4f0407))
* **types:** change optional parameter type from NotGiven to Omit ([5d3209e](https://github.com/greenflash-ai/python/commit/5d3209e6646e3c4b8166e9fc9e436559b7eb1d4f))

## 0.1.0-alpha.21 (2025-09-17)

Full Changelog: [v0.1.0-alpha.20...v0.1.0-alpha.21](https://github.com/greenflash-ai/python/compare/v0.1.0-alpha.20...v0.1.0-alpha.21)

### Features

* improve future compat with pydantic v3 ([3504aaa](https://github.com/greenflash-ai/python/commit/3504aaa75afaf69ae289441c0cef68bd66bdb3f0))
* **types:** replace List[str] with SequenceNotStr in params ([71c3998](https://github.com/greenflash-ai/python/commit/71c39986cdf27592e30f91256392dba01200abda))


### Bug Fixes

* avoid newer type syntax ([8d58bca](https://github.com/greenflash-ai/python/commit/8d58bca83fb69fae469c62a123046263a73c9e97))


### Chores

* **internal:** add Sequence related utils ([72cc80d](https://github.com/greenflash-ai/python/commit/72cc80d65296b9668aaf99f1a97f659fe407aae5))
* **internal:** move mypy configurations to `pyproject.toml` file ([a185c72](https://github.com/greenflash-ai/python/commit/a185c720b4cb869851132d0d08c0b32268071f71))
* **internal:** update pydantic dependency ([8f88e90](https://github.com/greenflash-ai/python/commit/8f88e90e7e6b782724da028756895ead3b45d1c9))
* **internal:** update pyright exclude list ([6813265](https://github.com/greenflash-ai/python/commit/6813265f97b18903115d09e6e8524a284212985f))
* **tests:** simplify `get_platform` test ([07ab091](https://github.com/greenflash-ai/python/commit/07ab091aff213eabb7ae6e0ae5095f3dad147ae4))

## 0.1.0-alpha.20 (2025-08-26)

Full Changelog: [v0.1.0-alpha.19...v0.1.0-alpha.20](https://github.com/greenflash-ai/python/compare/v0.1.0-alpha.19...v0.1.0-alpha.20)

### Chores

* **internal:** change ci workflow machines ([2be4f09](https://github.com/greenflash-ai/python/commit/2be4f09577140eb0f2b9a4e27e7e0ff3d08d6021))
* update github action ([ad2e871](https://github.com/greenflash-ai/python/commit/ad2e871bbe5feaf7946f5abcb05ab4b5be440d1e))
* update SDK preview from latest OpenAPI spec ([835b699](https://github.com/greenflash-ai/python/commit/835b699c2d5d33a33096661fd8dc9b964ea0a071))

## 0.1.0-alpha.19 (2025-08-10)

Full Changelog: [v0.1.0-alpha.18...v0.1.0-alpha.19](https://github.com/greenflash-ai/python/compare/v0.1.0-alpha.18...v0.1.0-alpha.19)

### Chores

* **internal:** update comment in script ([057d62c](https://github.com/greenflash-ai/python/commit/057d62c099f5116d51c7a1d1de4101da66702864))
* update @stainless-api/prism-cli to v5.15.0 ([743f2a2](https://github.com/greenflash-ai/python/commit/743f2a2aa59d351b9dcac900604b9e849895d8b5))

## 0.1.0-alpha.18 (2025-08-06)

Full Changelog: [v0.1.0-alpha.17...v0.1.0-alpha.18](https://github.com/greenflash-ai/python/compare/v0.1.0-alpha.17...v0.1.0-alpha.18)

### Chores

* **internal:** fix ruff target version ([afac1f2](https://github.com/greenflash-ai/python/commit/afac1f2690faf9cb11bf470c3c0bd52ecc739486))

## 0.1.0-alpha.17 (2025-07-31)

Full Changelog: [v0.1.0-alpha.16...v0.1.0-alpha.17](https://github.com/greenflash-ai/python/compare/v0.1.0-alpha.16...v0.1.0-alpha.17)

### Features

* **client:** support file upload requests ([085ba90](https://github.com/greenflash-ai/python/commit/085ba90d92cf23b25d6e083afc1af1343d7e3565))

## 0.1.0-alpha.16 (2025-07-30)

Full Changelog: [v0.1.0-alpha.15...v0.1.0-alpha.16](https://github.com/greenflash-ai/python/compare/v0.1.0-alpha.15...v0.1.0-alpha.16)

### Features

* **api:** manual updates ([757505f](https://github.com/greenflash-ai/python/commit/757505f93ab46214f699ba52f8c6689846c112c2))

## 0.1.0-alpha.15 (2025-07-27)

Full Changelog: [v0.1.0-alpha.14...v0.1.0-alpha.15](https://github.com/greenflash-ai/python/compare/v0.1.0-alpha.14...v0.1.0-alpha.15)

### Features

* **api:** manual updates ([5f77c93](https://github.com/greenflash-ai/python/commit/5f77c9308e3560443e88c4026affdb7324f61746))

## 0.1.0-alpha.14 (2025-07-27)

Full Changelog: [v0.1.0-alpha.13...v0.1.0-alpha.14](https://github.com/greenflash-ai/python/compare/v0.1.0-alpha.13...v0.1.0-alpha.14)

### Features

* **api:** manual updates ([219e7c2](https://github.com/greenflash-ai/python/commit/219e7c233e96246bb41d68a9671c0f03de08fc08))


### Chores

* update SDK preview from latest OpenAPI spec ([fd4a512](https://github.com/greenflash-ai/python/commit/fd4a512fb2bd72770be95f14655af007bbcea992))

## 0.1.0-alpha.13 (2025-07-25)

Full Changelog: [v0.1.0-alpha.12...v0.1.0-alpha.13](https://github.com/greenflash-ai/python/compare/v0.1.0-alpha.12...v0.1.0-alpha.13)

### Chores

* **project:** add settings file for vscode ([ee68cef](https://github.com/greenflash-ai/python/commit/ee68cef4af865b09b76ee193c4123bee50ef7a78))

## 0.1.0-alpha.12 (2025-07-23)

Full Changelog: [v0.1.0-alpha.11...v0.1.0-alpha.12](https://github.com/greenflash-ai/python/compare/v0.1.0-alpha.11...v0.1.0-alpha.12)

### Bug Fixes

* **parsing:** parse extra field types ([d71ef29](https://github.com/greenflash-ai/python/commit/d71ef29551c3e051a0bd9441ac4e6539ce12aa0e))

## 0.1.0-alpha.11 (2025-07-22)

Full Changelog: [v0.1.0-alpha.10...v0.1.0-alpha.11](https://github.com/greenflash-ai/python/compare/v0.1.0-alpha.10...v0.1.0-alpha.11)

### Bug Fixes

* **parsing:** ignore empty metadata ([52ffaf5](https://github.com/greenflash-ai/python/commit/52ffaf52a8a9549ea31ab90258172f7dad29dff2))

## 0.1.0-alpha.10 (2025-07-16)

Full Changelog: [v0.1.0-alpha.9...v0.1.0-alpha.10](https://github.com/greenflash-ai/python/compare/v0.1.0-alpha.9...v0.1.0-alpha.10)

### Features

* **api:** manual updates ([3c2c8f0](https://github.com/greenflash-ai/python/commit/3c2c8f06e3857e66a7b69862408d8801657ce659))

## 0.1.0-alpha.9 (2025-07-16)

Full Changelog: [v0.1.0-alpha.8...v0.1.0-alpha.9](https://github.com/greenflash-ai/python/compare/v0.1.0-alpha.8...v0.1.0-alpha.9)

### Features

* **api:** manual updates ([e8c6148](https://github.com/greenflash-ai/python/commit/e8c61489e7d62904e3374ca758e2a0598f682702))
* **api:** manual updates ([b6c96d1](https://github.com/greenflash-ai/python/commit/b6c96d178ee487d96a3e7f7ac76618cc2a63241f))
* **api:** manual updates ([5191242](https://github.com/greenflash-ai/python/commit/5191242eec24b127b45c685dee713ac594ffc94c))
* **api:** manual updates ([106a53a](https://github.com/greenflash-ai/python/commit/106a53a65052605b46a881148e3e58180bc1b6cf))


### Chores

* update SDK settings ([6534280](https://github.com/greenflash-ai/python/commit/65342808d7b94310c586eaf03fbf95fcb519b62e))

## 0.1.0-alpha.8 (2025-07-15)

Full Changelog: [v0.1.0-alpha.7...v0.1.0-alpha.8](https://github.com/greenflash-ai/python/compare/v0.1.0-alpha.7...v0.1.0-alpha.8)

### Features

* clean up environment call outs ([26dae3f](https://github.com/greenflash-ai/python/commit/26dae3f89b18c9fd0e2a8cb67c06e41dac85b78d))


### Bug Fixes

* **client:** don't send Content-Type header on GET requests ([0a99115](https://github.com/greenflash-ai/python/commit/0a9911546ece38d7291bacd6bfd2c20cd93f83fc))

## 0.1.0-alpha.7 (2025-07-11)

Full Changelog: [v0.1.0-alpha.6...v0.1.0-alpha.7](https://github.com/greenflash-ai/python/compare/v0.1.0-alpha.6...v0.1.0-alpha.7)

### Features

* **api:** update via SDK Studio ([0210ab0](https://github.com/greenflash-ai/python/commit/0210ab0278c2b3671ffda8739ca86fceca4329a0))
* **api:** update via SDK Studio ([836936c](https://github.com/greenflash-ai/python/commit/836936c7d4ba33e3b3d505825a109cdca3fca052))
* **api:** update via SDK Studio ([bd820b1](https://github.com/greenflash-ai/python/commit/bd820b145c606529e0c417941ca846e9f584582a))

## 0.1.0-alpha.6 (2025-07-11)

Full Changelog: [v0.1.0-alpha.5...v0.1.0-alpha.6](https://github.com/greenflash-ai/python/compare/v0.1.0-alpha.5...v0.1.0-alpha.6)

### Features

* **api:** update via SDK Studio ([69f3681](https://github.com/greenflash-ai/python/commit/69f368198a3db3c17ab739a565e6689f3f9e9e52))
* **api:** update via SDK Studio ([c658099](https://github.com/greenflash-ai/python/commit/c658099d8d4375b0aa82dd13c8fb510aad202dfe))
* **api:** update via SDK Studio ([0680595](https://github.com/greenflash-ai/python/commit/06805958d60a1c1466ca1e296191999470431a4e))


### Chores

* update SDK settings ([874a6e7](https://github.com/greenflash-ai/python/commit/874a6e71bdc746659737dac133fb01fe251074e7))

## 0.1.0-alpha.5 (2025-07-11)

Full Changelog: [v0.1.0-alpha.4...v0.1.0-alpha.5](https://github.com/greenflash-ai/python/compare/v0.1.0-alpha.4...v0.1.0-alpha.5)

### Chores

* **internal:** version bump ([ba385a4](https://github.com/greenflash-ai/python/commit/ba385a4c4f4f35c7f0c37eed452d1a606aed3758))

## 0.1.0-alpha.4 (2025-07-11)

Full Changelog: [v0.1.0-alpha.3...v0.1.0-alpha.4](https://github.com/greenflash-ai/python/compare/v0.1.0-alpha.3...v0.1.0-alpha.4)

### Chores

* **internal:** codegen related update ([084e7cf](https://github.com/greenflash-ai/python/commit/084e7cf7b896d1b965d4e78b9693c61bc277ab6b))
* **internal:** version bump ([851db65](https://github.com/greenflash-ai/python/commit/851db6588128dd72d9f6dfd284872df1daf9c5aa))
* **readme:** fix version rendering on pypi ([0c61810](https://github.com/greenflash-ai/python/commit/0c61810050e91daf95abfdf1c41dee883eddd0c3))

## 0.1.0-alpha.3 (2025-07-11)

Full Changelog: [v0.1.0-alpha.2...v0.1.0-alpha.3](https://github.com/greenflash-ai/python/compare/v0.1.0-alpha.2...v0.1.0-alpha.3)

### Features

* **api:** update via SDK Studio ([1f79f04](https://github.com/greenflash-ai/python/commit/1f79f0435f81adbb6dea933e848e494c87129b15))
* **api:** update via SDK Studio ([c713904](https://github.com/greenflash-ai/python/commit/c7139040e0ad0a006a9eef001400273b86e3f4ee))

## 0.1.0-alpha.2 (2025-07-11)

Full Changelog: [v0.1.0-alpha.1...v0.1.0-alpha.2](https://github.com/greenflash-ai/python/compare/v0.1.0-alpha.1...v0.1.0-alpha.2)

### Features

* **api:** update via SDK Studio ([964401f](https://github.com/greenflash-ai/python/commit/964401fc840c7d188f5125ff1f6a12e787d85ad4))

## 0.1.0-alpha.1 (2025-07-09)

Full Changelog: [v0.0.1-alpha.0...v0.1.0-alpha.1](https://github.com/greenflash-ai/python/compare/v0.0.1-alpha.0...v0.1.0-alpha.1)

### Features

* **api:** update via SDK Studio ([6675f34](https://github.com/greenflash-ai/python/commit/6675f34410ea25b5251e3815114073b0a70de4ce))


### Chores

* update SDK settings ([0ed597f](https://github.com/greenflash-ai/python/commit/0ed597fa0c193b51228497dcb5c0cd732135e1f0))
* update SDK settings ([f67dad2](https://github.com/greenflash-ai/python/commit/f67dad26f22148bfe122e939b7bc6c4bf904a7d7))
