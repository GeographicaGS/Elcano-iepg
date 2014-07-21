# coding=UTF8

"""
Constants
"""
import blockfunctions

backend = {
    'autoAuth': False,
    'DocumentListLength': 16,
    'UnpublishedHighlightCatalogBackendListLength': 16,
    "newsCatalogPageSize": 16
}

frontend = {
    "documentCatalogListSize": 16,
    "newsCatalogPageSize": 16,
    "maxTweets": 15
}

lang = ["en", "es"]

years = [1990, 1995, 2000, 2005, 2010, 2011, 2012, 2013]

dimensions = {
    "economic_global": ["energy", "primary_goods", "manufactures", "services", "investments"],
    "military_global": ["troops", "military_equipment"],
    "soft_global": ["migrations", "tourism", "sports", "culture", "information", "technology", 
                    "science", "education", "cooperation"]
}

variableNames = {
    "iepg": {
        "energy": {
            "order": 0,
            "column": "energy",
            "coeficient": 0.0695,
            "name_en": "Energy",
            "name_es": "Energía"},
        "primary_goods": {
            "order": 5,
            "column": "primary_goods",
            "coeficient": 0.0513,
            "name_en": "Primary Goods",
            "name_es": "Bienes primarios"},
        "manufactures": {
            "order": 10,
            "column": "manufactures",
            "coeficient": 0.0744,
            "name_en": "Manufactures",
            "name_es": "Manufacturas"},
        "services": {
            "order": 15,
            "column": "services",
            "coeficient": 0.0888,
            "name_en": "Services",
            "name_es": "Servicios"},
        "investments": {
            "order": 20,
            "column": "investments",
            "coeficient": 0.101,
            "name_en": "Investments",
            "name_es": "Inversiones"},
        "troops": {
            "order": 25,
            "column": "troops",
            "coeficient": 0.0795,
            "name_en": "Troops",
            "name_es": "Tropas"},
        "military_equipment": {
            "order": 30,
            "column": "military_equipment",
            "coeficient": 0.0757,
            "name_en": "Military Equipment",
            "name_es": "Equipo militar"},
        "migrations": {
            "order": 35,
            "column": "migrations",
            "coeficient": 0.0411,
            "name_en": "Migrations",
            "name_es": "Migraciones"},
        "tourism": {
            "order": 40,
            "column": "tourism",
            "coeficient": 0.041,
            "name_en": "Tourism",
            "name_es": "Turismo"},
        "sports": {
            "order": 45,
            "column": "sports",
            "coeficient": 0.0342,
            "name_en": "Sports",
            "name_es": "Deportes"},
        "culture": {
            "order": 50,
            "column": "culture",
            "coeficient": 0.0698,
            "name_en": "Culture",
            "name_es": "Cultura"},
        "information": {
            "order": 55,
            "column": "information",
            "coeficient": 0.0599,
            "name_en": "Information",
            "name_es": "Información"},
        "technology": {
            "order": 60,
            "column": "technology",
            "coeficient": 0.0582,
            "name_en": "Technology",
            "name_es": "Tecnología"},
        "science": {
            "order": 65,
            "column": "science",
            "coeficient": 0.0571,
            "name_en": "Science",
            "name_es": "Ciencia"},
        "education": {
            "order": 70,
            "column": "education",
            "coeficient": 0.0545,
            "name_en": "Education",
            "name_es": "Educación"},
        "cooperation": {
            "order": 75,
            "column": "cooperation",
            "coeficient": 0.044,
            "name_en": "Cooperation",
            "name_es": "Cooperación"},
        "economic_global": {
            "order": 80,
            "column": "economic_presence",
            "coeficient": 1,
            "name_en": "Economic Presence",
            "name_es": "Presencia económica"},
        "military_global": {
            "order": 85,
            "column": "military_presence",
            "coeficient": 1,
            "name_en": "Military Presence",
            "name_es": "Presencia militar"},
        "soft_global": {
            "order": 90,
            "column": "soft_presence",
            "coeficient": 1,
            "name_en": "Soft Presence",
            "name_es": "Presencia blanda"},
        "global": {
            "order": 95,
            "column": "iepg",
            "coeficient": 1,
            "name_en": "IEPG",
            "name_es": "IEPG"}
    },
    "iepe": {
        "energy": {
            "order": 1000,
            "column": "energy",
            "coeficient": 0.0695,
            "name_en": "Energy",
            "name_es": "Energía"},
        "primary_goods": {
            "order": 1005,
            "column": "primary_goods",
            "coeficient": 0.0513,
            "name_en": "Primary Goods",
            "name_es": "Bienes primarios"},
        "manufactures": {
            "order": 1010,
            "column": "manufactures",
            "coeficient": 0.0744,
            "name_en": "Manufactures",
            "name_es": "Manufacturas"},
        "services": {
            "order": 1015,
            "column": "services",
            "coeficient": 0.0888,
            "name_en": "Services",
            "name_es": "Servicios"},
        "investments": {
            "order": 1020,
            "column": "investments",
            "coeficient": 0.101,
            "name_en": "Investments",
            "name_es": "Inversiones"},
        "troops": {
            "order": 1025,
            "column": "troops",
            "coeficient": 0.0795,
            "name_en": "Troops",
            "name_es": "Tropas"},
        "military_equipment": {
            "order": 1030,
            "column": "military_equipment",
            "coeficient": 0.0757,
            "name_en": "Military Equipment",
            "name_es": "Equipo militar"},
        "migrations": {
            "order": 1035,
            "column": "migrations",
            "coeficient": 0.0411,
            "name_en": "Migrations",
            "name_es": "Migraciones"},
        "tourism": {
            "order": 1040,
            "column": "tourism",
            "coeficient": 0.041,
            "name_en": "Tourism",
            "name_es": "Turismo"},
        "sports": {
            "order": 1045,
            "column": "sports",
            "coeficient": 0.0342,
            "name_en": "Sports",
            "name_es": "Deportes"},
        "culture": {
            "order": 1050,
            "column": "culture",
            "coeficient": 0.0698,
            "name_en": "Culture",
            "name_es": "Cultura"},
        "information": {
            "order": 1055,
            "column": "information",
            "coeficient": 0.0599,
            "name_en": "Information",
            "name_es": "Información"},
        "technology": {
            "order": 1060,
            "column": "technology",
            "coeficient": 0.0582,
            "name_en": "Technology",
            "name_es": "Tecnología"},
        "science": {
            "order": 1065,
            "column": "science",
            "coeficient": 0.0571,
            "name_en": "Science",
            "name_es": "Ciencia"},
        "education": {
            "order": 1070,
            "column": "education",
            "coeficient": 0.0545,
            "name_en": "Education",
            "name_es": "Educación"},
        "cooperation": {
            "order": 1075,
            "column": "cooperation",
            "coeficient": 0.044,
            "name_en": "Cooperation",
            "name_es": "Cooperación"},
        "economic_global": {
            "order": 1080,
            "column": "economic_presence",
            "name_en": "Economic Presence",
            "name_es": "Presencia económica"},
        "military_global": {
            "order": 1085,
            "column": "military_presence",
            "name_en": "Military Presence",
            "name_es": "Presencia militar"},
        "soft_global": {
            "order": 1090,
            "column": "soft_presence",
            "name_en": "Soft Presence",
            "name_es": "Presencia blanda"},
        "global": {
            "order": 1095,
            "column": "iepe",
            "name_en": "IEPE",
            "name_es": "IEPE"}
    },
    "context": {
        "gdp": {
            "column": "pib",
            "name_en": "GDP",
            "name_es": "PIB"},
        "population": {
            "column": "population",
            "name_en": "Population",
            "name_es": "Población"}
    },
    "iepe_individual_contribution": {
        "energy": {
            "column": "energy",
            "name_en": "Energy",
            "name_es": "Energía"},
        "primary_goods": {
            "column": "primary_goods",
            "name_en": "Primary Goods",
            "name_es": "Bienes primarios"},
        "manufactures": {
            "column": "manufactures",
            "name_en": "Manufactures",
            "name_es": "Manufacturas"},
        "services": {
            "column": "services",
            "name_en": "Services",
            "name_es": "Servicios"},
        "investments": {
            "column": "investments",
            "name_en": "Investments",
            "name_es": "Inversiones"},
        "troops": {
            "column": "troops",
            "name_en": "Troops",
            "name_es": "Tropas"},
        "military_equipment": {
            "column": "military_equipment",
            "name_en": "Military Equipment",
            "name_es": "Equipo militar"},
        "migrations": {
            "column": "migrations",
            "name_en": "Migrations",
            "name_es": "Migraciones"},
        "tourism": {
            "column": "tourism",
            "name_en": "Tourism",
            "name_es": "Turismo"},
        "sports": {
            "column": "sports",
            "name_en": "Sports",
            "name_es": "Deportes"},
        "culture": {
            "column": "culture",
            "name_en": "Culture",
            "name_es": "Cultura"},
        "information": {
            "column": "information",
            "name_en": "Information",
            "name_es": "Información"},
        "technology": {
            "column": "technology",
            "name_en": "Technology",
            "name_es": "Tecnología"},
        "science": {
            "column": "science",
            "name_en": "Science",
            "name_es": "Ciencia"},
        "education": {
            "column": "education",
            "name_en": "Education",
            "name_es": "Educación"},
        "cooperation": {
            "column": "cooperation",
            "name_en": "Cooperation",
            "name_es": "Cooperación"},
        "economic_global": {
            "column": "economic_contribution",
            "name_en": "Economic Contribution",
            "name_es": "Contribución económica"},
        "military_global": {
            "column": "military_contribution",
            "name_en": "Military Contribution",
            "name_es": "Contribución militar"},
        "soft_global": {
            "column": "soft_contribution",
            "name_en": "Soft Contribution",
            "name_es": "Contribución blanda"}
    },
    "iepe_quota": {
        "global_global": {
            "column": "global_quota",
            "name_en": "Global Quota",
            "name_es": "Cuota global"},
        "economic_global": {
            "column": "economic_quota",
            "name_en": "Economic Quota",
            "name_es": "Cuota económica"},
        "soft_global": {
            "column": "soft_quota",
            "name_en": "Soft Quota",
            "name_es": "Cuota blanda"}
    },
    "iepe_relative_contribution": {
        "energy": {
            "column": "energy",
            "name_en": "Energy",
            "name_es": "Energía"},
        "primary_goods": {
            "column": "primary_goods",
            "name_en": "Primary Goods",
            "name_es": "Bienes primarios"},
        "manufactures": {
            "column": "manufactures",
            "name_en": "Manufactures",
            "name_es": "Manufacturas"},
        "services": {
            "column": "services",
            "name_en": "Services",
            "name_es": "Servicios"},
        "investments": {
            "column": "investments",
            "name_en": "Investments",
            "name_es": "Inversiones"},
        "troops": {
            "column": "troops",
            "name_en": "Troops",
            "name_es": "Tropas"},
        "military_equipment": {
            "column": "military_equipment",
            "name_en": "Military Equipment",
            "name_es": "Equipo militar"},
        "migrations": {
            "column": "migrations",
            "name_en": "Migrations",
            "name_es": "Migraciones"},
        "tourism": {
            "column": "tourism",
            "name_en": "Tourism",
            "name_es": "Turismo"},
        "sports": {
            "column": "sports",
            "name_en": "Sports",
            "name_es": "Deportes"},
        "culture": {
            "column": "culture",
            "name_en": "Culture",
            "name_es": "Cultura"},
        "information": {
            "column": "information",
            "name_en": "Information",
            "name_es": "Información"},
        "technology": {
            "column": "technology",
            "name_en": "Technology",
            "name_es": "Tecnología"},
        "science": {
            "column": "science",
            "name_en": "Science",
            "name_es": "Ciencia"},
        "education": {
            "column": "education",
            "name_en": "Education",
            "name_es": "Educación"},
        "cooperation": {
            "column": "cooperation",
            "name_en": "Cooperation",
            "name_es": "Cooperación"},
        "economic_global": {
            "column": "economic_contribution",
            "name_en": "Economic Contribution",
            "name_es": "Contribución económica"},
        "military_global": {
            "column": "military_contribution",
            "name_en": "Military Contribution",
            "name_es": "Contribución militar"},
        "soft_global": {
            "column": "soft_contribution",
            "name_en": "Soft Contribution",
            "name_es": "Contribución blanda"}
    },
    "iepg_individual_contribution": {
        "energy": {
            "column": "energy",
            "name_en": "Energy",
            "name_es": "Energía"},
        "primary_goods": {
            "column": "primary_goods",
            "name_en": "Primary Goods",
            "name_es": "Bienes primarios"},
        "manufactures": {
            "column": "manufactures",
            "name_en": "Manufactures",
            "name_es": "Manufacturas"},
        "services": {
            "column": "services",
            "name_en": "Services",
            "name_es": "Servicios"},
        "investments": {
            "column": "investments",
            "name_en": "Investments",
            "name_es": "Inversiones"},
        "troops": {
            "column": "troops",
            "name_en": "Troops",
            "name_es": "Tropas"},
        "military_equipment": {
            "column": "military_equipment",
            "name_en": "Military Equipment",
            "name_es": "Equipo militar"},
        "migrations": {
            "column": "migrations",
            "name_en": "Migrations",
            "name_es": "Migraciones"},
        "tourism": {
            "column": "tourism",
            "name_en": "Tourism",
            "name_es": "Turismo"},
        "sports": {
            "column": "sports",
            "name_en": "Sports",
            "name_es": "Deportes"},
        "culture": {
            "column": "culture",
            "name_en": "Culture",
            "name_es": "Cultura"},
        "information": {
            "column": "information",
            "name_en": "Information",
            "name_es": "Información"},
        "technology": {
            "column": "technology",
            "name_en": "Technology",
            "name_es": "Tecnología"},
        "science": {
            "column": "science",
            "name_en": "Science",
            "name_es": "Ciencia"},
        "education": {
            "column": "education",
            "name_en": "Education",
            "name_es": "Educación"},
        "cooperation": {
            "column": "cooperation",
            "name_en": "Cooperation",
            "name_es": "Cooperación"},
        "economic_global": {
            "column": "economic_contribution",
            "name_en": "Economic Contribution",
            "name_es": "Contribución económica"},
        "military_global": {
            "column": "military_contribution",
            "name_en": "Military Contribution",
            "name_es": "Contribución militar"},
        "soft_global": {
            "column": "soft_contribution",
            "name_en": "Soft Contribution",
            "name_es": "Contribución blanda"}
    },
    "iepg_quota": {
        "global_global": {
            "column": "global_quota",
            "name_en": "Global Quota",
            "name_es": "Cuota global"},
        "economic_global": {
            "column": "economic_quota",
            "name_en": "Economic Quota",
            "name_es": "Cuota económica"},
        "soft_global": {
            "column": "soft_quota",
            "name_en": "Soft Quota",
            "name_es": "Cuota blanda"},
        "military_global": {
            "column": "military_quota",
            "name_en": "Military Quota",
            "name_es": "Cuota militar"}
    },
    "iepg_relative_contribution": {
        "energy": {
            "column": "energy",
            "name_en": "Energy",
            "name_es": "Energía"},
        "primary_goods": {
            "column": "primary_goods",
            "name_en": "Primary Goods",
            "name_es": "Bienes primarios"},
        "manufactures": {
            "column": "manufactures",
            "name_en": "Manufactures",
            "name_es": "Manufacturas"},
        "services": {
            "column": "services",
            "name_en": "Services",
            "name_es": "Servicios"},
        "investments": {
            "column": "investments",
            "name_en": "Investments",
            "name_es": "Inversiones"},
        "troops": {
            "column": "troops",
            "name_en": "Troops",
            "name_es": "Tropas"},
        "military_equipment": {
            "column": "military_equipment",
            "name_en": "Military Equipment",
            "name_es": "Equipo militar"},
        "migrations": {
            "column": "migrations",
            "name_en": "Migrations",
            "name_es": "Migraciones"},
        "tourism": {
            "column": "tourism",
            "name_en": "Tourism",
            "name_es": "Turismo"},
        "sports": {
            "column": "sports",
            "name_en": "Sports",
            "name_es": "Deportes"},
        "culture": {
            "column": "culture",
            "name_en": "Culture",
            "name_es": "Cultura"},
        "information": {
            "column": "information",
            "name_en": "Information",
            "name_es": "Información"},
        "technology": {
            "column": "technology",
            "name_en": "Technology",
            "name_es": "Tecnología"},
        "science": {
            "column": "science",
            "name_en": "Science",
            "name_es": "Ciencia"},
        "education": {
            "column": "education",
            "name_en": "Education",
            "name_es": "Educación"},
        "cooperation": {
            "column": "cooperation",
            "name_en": "Cooperation",
            "name_es": "Cooperación"},
        "economic_global": {
            "column": "economic_contribution",
            "name_en": "Economic Contribution",
            "name_es": "Contribución económica"},
        "military_global": {
            "column": "military_contribution",
            "name_en": "Military Contribution",
            "name_es": "Contribución militar"},
        "soft_global": {
            "column": "soft_contribution",
            "name_en": "Soft Contribution",
            "name_es": "Contribución blanda"}
    }
}


























# TODO: To be deprecated
frontend_errors = {
    "-1": {"Code": "-1", "Error": "Unknown language."},
    "-3": {"Code": "-3", "Error": "Invalid offset."},
    "-4": {"Code": "-4", "Error": "Unknown Twitter user."},
    "-5": {"Code": "-5", "Error": "Invalid label ID."}
}

# TODO: To be deprecated
model_errors = {
    "-1": {"Code": "-1", "Error": "Unknown language."},
    "-2": {"Code": "-2", "Error": "Unknown news section."},
    "-3": {"Code": "-3", "Error": "Invalid number."},
    "-4": {"Code": "-4", "Error": "Unknown Twitter user."}
}

# TODO: to be deprecated
years = [1990, 1995, 2000, 2005, 2010, 2011, 2012, 2013]

# TODO: to be deprecated
families = ["iepg", "iepe", "context"]

# TODO: to be deprecated
blocks = {
    "XBEU": {
        "key": "european_union",
        "name_en": "European Union",
        "name_es": "Unión Europea",
        "members": {
            "1990": {
                "countries": ["IE"],
                "precalculated": True
            },
            "1995": {
                "countries": ["FR", "IE"],
                "precalculated": True
            },
            "2000": {
                "countries": ["ES", "FR", "IE"],
                "precalculated": True
            },
            "2005": {
                "countries": ["DE", "ES", "FR", "IE"],
                "precalculated": True
            },
            "2010": {
                "countries": ["DE", "NL", "ES", "FR", "IE"],
                "precalculated": True
            },
            "2011": {
                "countries": ["DE", "NL", "IT", "ES", "FR", "IE"],
                "precalculated": True
            },
            "2012": {
                "countries": ["DE", "NL", "IT", "SE", "ES", "FR", "IE"],
                "precalculated": True
            },
            "2013": {
                "countries": ["DE", "NL", "IT", "SE", "PL", "ES", "FR", "IE"],
                "precalculated": True
            }
        }
    }
    # "XBE2": {
    #     "key": "europe",
    #     "name_en": "Europe",
    #     "name_es": "Europa",
    #     "members": {
    #         "1990": ["ES", "FR", "IE"],
    #         "1995": ["ES", "FR", "IE"],
    #         "2000": ["ES", "FR", "IE"],
    #         "2005": ["ES", "FR", "IE"],
    #         "2010": ["ES", "FR", "IE"],
    #         "2011": ["ES", "FR", "IE"],
    #         "2012": ["ES", "FR", "IE"],
    #         "2013": ["ES", "FR", "IE"]
    #     }
    # },
    # "XBLA": {
    #     "key": "latin_america",
    #     "precalculated": False,
    #     "name_en": "Latin America",
    #     "name_es": "América Latina",
    #     "members": {
    #         "1990": ["ES", "FR", "IE"],
    #         "1995": ["ES", "FR", "IE"],
    #         "2000": ["ES", "FR", "IE"],
    #         "2005": ["ES", "FR", "IE"],
    #         "2010": ["ES", "FR", "IE"],
    #         "2011": ["ES", "FR", "IE"],
    #         "2012": ["ES", "FR", "IE"],
    #         "2013": ["ES", "FR", "IE"]
    #     }
    # },
    # "XBNA": {
    #     "key": "north_america",
    #     "precalculated": False,
    #     "name_en": "North America",
    #     "name_es": "América del Norte",
    #     "members": {
    #         "1990": ["ES", "FR", "IE"],
    #         "1995": ["ES", "FR", "IE"],
    #         "2000": ["ES", "FR", "IE"],
    #         "2005": ["ES", "FR", "IE"],
    #         "2010": ["ES", "FR", "IE"],
    #         "2011": ["ES", "FR", "IE"],
    #         "2012": ["ES", "FR", "IE"],
    #         "2013": ["ES", "FR", "IE"]
    #     }
    # },
    # "XBAP": {
    #     "key": "asia_and_pacific",
    #     "precalculated": False,
    #     "name_en": "Asia & Pacific",
    #     "name_es": "Ásia y Pacífico",
    #     "members": {
    #         "1990": ["ES", "FR", "IE"],
    #         "1995": ["ES", "FR", "IE"],
    #         "2000": ["ES", "FR", "IE"],
    #         "2005": ["ES", "FR", "IE"],
    #         "2010": ["ES", "FR", "IE"],
    #         "2011": ["ES", "FR", "IE"],
    #         "2012": ["ES", "FR", "IE"],
    #         "2013": ["ES", "FR", "IE"]
    #     }
    # },
    # "XBME": {
    #     "key": "magreb_middle_east",
    #     "precalculated": False,
    #     "name_en": "Magreb & Middle East",
    #     "name_es": "Magreb y Oriente Medio",
    #     "members": {
    #         "1990": ["ES", "FR", "IE"],
    #         "1995": ["ES", "FR", "IE"],
    #         "2000": ["ES", "FR", "IE"],
    #         "2005": ["ES", "FR", "IE"],
    #         "2010": ["ES", "FR", "IE"],
    #         "2011": ["ES", "FR", "IE"],
    #         "2012": ["ES", "FR", "IE"],
    #         "2013": ["ES", "FR", "IE"]
    #     }
    # }
}


# TODO: to be deprecated
variables = {
    "iepg_energy": {
        "key": "energy",
        "precalculus": "",
        "family": "iepg",
        "name_en": "Energy",
        "name_es": "Energía",
        "table": "iepg_data.iepg_final_data",
        "column": "energy"},
    "iepg_primary_goods": {
        "key": "primary_goods",
        "precalculus": "",
        "family": "iepg",
        "name_en": "Primary Goods",
        "name_es": "Bienes primarios",
        "table": "iepg_data.iepg_final_data",
        "column": "primary_goods"},
    "iepg_manufactures": {
        "key": "manufactures",
        "precalculus": "",
        "family": "iepg",
        "name_en": "Manufactures",
        "name_es": "Manufacturas",
        "table": "iepg_data.iepg_final_data",
        "column": "manufactures"},
    "iepg_services": {
        "key": "services",
        "precalculus": "",
        "family": "iepg",
        "name_en": "Services",
        "name_es": "Servicios",
        "table": "iepg_data.iepg_final_data",
        "column": "services"},
    "iepg_investments": {
        "key": "investments",
        "precalculus": "",
        "family": "iepg",
        "name_en": "Investments",
        "name_es": "Inversiones",
        "table": "iepg_data.iepg_final_data",
        "column": "investments"},
    "iepg_troops": {
        "key": "troops",
        "precalculus": "",
        "family": "iepg",
        "name_en": "Troops",
        "name_es": "Tropas",
        "table": "iepg_data.iepg_final_data",
        "column": "troops"},
    "iepg_military_equipment": {
        "key": "military_equipment",
        "precalculus": "",
        "family": "iepg",
        "name_en": "Military Equipment",
        "name_es": "Equipo militar",
        "table": "iepg_data.iepg_final_data",
        "column": "military_equipment"},
    "iepg_migrations": {
        "key": "migrations",
        "precalculus": "",
        "family": "iepg",
        "name_en": "Migrations",
        "name_es": "Migraciones",
        "table": "iepg_data.iepg_final_data",
        "column": "migrations"},
    "iepg_tourism": {
        "key": "tourism",
        "precalculus": "",
        "family": "iepg",
        "name_en": "Tourism",
        "name_es": "Turismo",
        "table": "iepg_data.iepg_final_data",
        "column": "tourism"},
    "iepg_sports": {
        "key": "sports",
        "precalculus": "",
        "family": "iepg",
        "name_en": "Sports",
        "name_es": "Deportes",
        "table": "iepg_data.iepg_final_data",
        "column": "sports"},
    "iepg_culture": {
        "key": "culture",
        "precalculus": "",
        "family": "iepg",
        "name_en": "Culture",
        "name_es": "Cultura",
        "table": "iepg_data.iepg_final_data",
        "column": "culture"},
    "iepg_information": {
        "key": "information",
        "precalculus": "",
        "family": "iepg",
        "name_en": "Information",
        "name_es": "Información",
        "table": "iepg_data.iepg_final_data",
        "column": "information"},
    "iepg_technology": {
        "key": "technology",
        "precalculus": "",
        "family": "iepg",
        "name_en": "Technology",
        "name_es": "Tecnología",
        "table": "iepg_data.iepg_final_data",
        "column": "technology"},
    "iepg_science": {
        "key": "science",
        "precalculus": "",
        "family": "iepg",
        "name_en": "Science",
        "name_es": "Ciencia",
        "table": "iepg_data.iepg_final_data",
        "column": "science"},
    "iepg_education": {
        "key": "education",
        "precalculus": "",
        "family": "iepg",
        "name_en": "Education",
        "name_es": "Educación",
        "table": "iepg_data.iepg_final_data",
        "column": "education"},
    "iepg_cooperation": {
        "key": "cooperation",
        "precalculus": "",
        "family": "iepg",
        "name_en": "Cooperation",
        "name_es": "Cooperación",
        "table": "iepg_data.iepg_final_data",
        "column": "cooperation"},
    "iepg_economic_presence": {
        "key": "economic_presence",
        "precalculus": "",
        "family": "iepg",
        "name_en": "Economic Presence",
        "name_es": "Presencia económica",
        "table": "iepg_data.iepg_final_data",
        "column": "economic_presence"},
    "iepg_military_presence": {
        "key": "military_presence",
        "precalculus": "",
        "family": "iepg",
        "name_en": "Military Presence",
        "name_es": "Presencia militar",
        "table": "iepg_data.iepg_final_data",
        "column": "military_presence"},
    "iepg_soft_presence": {
        "key": "soft_presence",
        "precalculus": "",
        "family": "iepg",
        "name_en": "Soft Presence",
        "name_es": "Presencia blanda",
        "table": "iepg_data.iepg_final_data",
        "column": "soft_presence"},
    "iepg": {
        "key": "iepg",
        "precalculus": "",
        "family": "iepg",
        "name_en": "IEPG",
        "name_es": "IEPG",
        "table": "iepg_data.iepg_final_data",
        "column": "iepg"},
    "iepe_energy": {
        "key": "energy",
        "precalculus": "",
        "family": "iepe",
        "name_en": "Energy",
        "name_es": "Energía",
        "table": "iepg_data.iepe_final_data",
        "column": "energy"},
    "iepe_primary_goods": {
        "key": "primary_goods",
        "precalculus": "",
        "family": "iepe",
        "name_en": "Primary Goods",
        "name_es": "Bienes primarios",
        "table": "iepg_data.iepe_final_data",
        "column": "primary_goods"},
    "iepe_manufactures": {
        "key": "manufactures",
        "precalculus": "",
        "family": "iepe",
        "name_en": "Manufactures",
        "name_es": "Manufacturas",
        "table": "iepg_data.iepe_final_data",
        "column": "manufactures"},
    "iepe_services": {
        "key": "services",
        "precalculus": "",
        "family": "iepe",
        "name_en": "Services",
        "name_es": "Servicios",
        "table": "iepg_data.iepe_final_data",
        "column": "services"},
    "iepe_investments": {
        "key": "investments",
        "precalculus": "",
        "family": "iepe",
        "name_en": "Investments",
        "name_es": "Inversiones",
        "table": "iepg_data.iepe_final_data",
        "column": "investments"},
    "iepe_troops": {
        "key": "troops",
        "precalculus": "",
        "family": "iepe",
        "name_en": "Troops",
        "name_es": "Tropas",
        "table": "iepg_data.iepe_final_data",
        "column": "troops"},
    "iepe_military_equipment": {
        "key": "military_equipment",
        "precalculus": "",
        "family": "iepe",
        "name_en": "Military Equipment",
        "name_es": "Equipo militar",
        "table": "iepg_data.iepe_final_data",
        "column": "military_equipment"},
    "iepe_migrations": {
        "key": "migrations",
        "precalculus": "",
        "family": "iepe",
        "name_en": "Migrations",
        "name_es": "Migraciones",
        "table": "iepg_data.iepe_final_data",
        "column": "migrations"},
    "iepe_tourism": {
        "key": "tourism",
        "precalculus": "",
        "family": "iepe",
        "name_en": "Tourism",
        "name_es": "Turismo",
        "table": "iepg_data.iepe_final_data",
        "column": "tourism"},
    "iepe_sports": {
        "key": "sports",
        "precalculus": "",
        "family": "iepe",
        "name_en": "Sports",
        "name_es": "Deportes",
        "table": "iepg_data.iepe_final_data",
        "column": "sports"},
    "iepe_culture": {
        "key": "culture",
        "precalculus": "",
        "family": "iepe",
        "name_en": "Culture",
        "name_es": "Cultura",
        "table": "iepg_data.iepe_final_data",
        "column": "culture"},
    "iepe_information": {
        "key": "information",
        "precalculus": "",
        "family": "iepe",
        "name_en": "Information",
        "name_es": "Información",
        "table": "iepg_data.iepe_final_data",
        "column": "information"},
    "iepe_technology": {
        "key": "technology",
        "precalculus": "",
        "family": "iepe",
        "name_en": "Technology",
        "name_es": "Tecnología",
        "table": "iepg_data.iepe_final_data",
        "column": "technology"},
    "iepe_science": {
        "key": "science",
        "precalculus": "",
        "family": "iepe",
        "name_en": "Science",
        "name_es": "Ciencia",
        "table": "iepg_data.iepe_final_data",
        "column": "science"},
    "iepe_education": {
        "key": "education",
        "precalculus": "",
        "family": "iepe",
        "name_en": "Education",
        "name_es": "Educación",
        "table": "iepg_data.iepe_final_data",
        "column": "education"},
    "iepe_cooperation": {
        "key": "cooperation",
        "precalculus": "",
        "family": "iepe",
        "name_en": "Cooperation",
        "name_es": "Cooperación",
        "table": "iepg_data.iepe_final_data",
        "column": "cooperation"},
    "iepe_economic_presence": {
        "key": "economic_presence",
        "precalculus": "",
        "family": "iepe",
        "name_en": "Economic Presence",
        "name_es": "Presencia económica",
        "table": "iepg_data.iepe_final_data",
        "column": "economic_presence"},
    "iepe_military_presence": {
        "key": "military_presence",
        "precalculus": "",
        "family": "iepe",
        "name_en": "Military Presence",
        "name_es": "Presencia militar",
        "table": "iepg_data.iepe_final_data",
        "column": "military_presence"},
    "iepe_soft_presence": {
        "key": "soft_presence",
        "precalculus": "",
        "family": "iepe",
        "name_en": "Soft Presence",
        "name_es": "Presencia blanda",
        "table": "iepg_data.iepe_final_data",
        "column": "soft_presence"},
    "iepe": {
        "key": "iepe",
        "precalculus": "",
        "family": "iepe",
        "name_en": "IEPE",
        "name_es": "IEPE",
        "table": "iepg_data.iepe_final_data",
        "column": "iepe"},
    # "iepg_ue_energy": {
    #     "key": "energy",
    #     "precalculus": "",
    #     "family": "iepg",
    #     "name_en": "Energy",
    #     "name_es": "Energía",
    #     "table": "iepg_data.iepg_final_data_ue",
    #     "column": "energy"},
    # "iepg_ue_primary_goods": {
    #     "key": "primary_goods",
    #     "precalculus": "eu",
    #     "family": "iepg",
    #     "name_en": "Primary Goods",
    #     "name_es": "Bienes primarios",
    #     "table": "iepg_data.iepg_final_data_ue",
    #     "column": "primary_goods"},
    # "iepg_ue_manufactures": {
    #     "key": "manufactures",
    #     "precalculus": "eu",
    #     "family": "iepg",
    #     "name_en": "Manufactures",
    #     "name_es": "Manufacturas",
    #     "table": "iepg_data.iepg_final_data_ue",
    #     "column": "manufactures"},
    # "iepg_ue_services": {
    #     "key": "services",
    #     "precalculus": "eu",
    #     "family": "iepg",
    #     "name_en": "Services",
    #     "name_es": "Servicios",
    #     "table": "iepg_data.iepg_final_data_ue",
    #     "column": "services"},
    # "iepg_ue_investments": {
    #     "key": "investments",
    #     "precalculus": "eu",
    #     "family": "iepg",
    #     "name_en": "Investments",
    #     "name_es": "Inversiones",
    #     "table": "iepg_data.iepg_final_data_ue",
    #     "column": "investments"},
    # "iepg_ue_troops": {
    #     "key": "troops",
    #     "precalculus": "eu",
    #     "family": "iepg",
    #     "name_en": "Troops",
    #     "name_es": "Tropas",
    #     "table": "iepg_data.iepg_final_data_ue",
    #     "column": "troops"},
    # "iepg_ue_military_equipment": {
    #     "key": "military_equipment",
    #     "precalculus": "eu",
    #     "family": "iepg",
    #     "name_en": "Military Equipment",
    #     "name_es": "Equipo militar",
    #     "table": "iepg_data.iepg_final_data_ue",
    #     "column": "military_equipment"},
    # "iepg_ue_migrations": {
    #     "key": "migrations",
    #     "precalculus": "eu",
    #     "family": "iepg",
    #     "name_en": "Migrations",
    #     "name_es": "Migraciones",
    #     "table": "iepg_data.iepg_final_data_ue",
    #     "column": "migrations"},
    # "iepg_ue_tourism": {
    #     "key": "tourism",
    #     "precalculus": "eu",
    #     "family": "iepg",
    #     "name_en": "Tourism",
    #     "name_es": "Turismo",
    #     "table": "iepg_data.iepg_final_data_ue",
    #     "column": "tourism"},
    # "iepg_ue_sports": {
    #     "key": "sports",
    #     "precalculus": "eu",
    #     "family": "iepg",
    #     "name_en": "Sports",
    #     "name_es": "Deportes",
    #     "table": "iepg_data.iepg_final_data_ue",
    #     "column": "sports"},
    # "iepg_ue_culture": {
    #     "key": "culture",
    #     "precalculus": "eu",
    #     "family": "iepg",
    #     "name_en": "Culture",
    #     "name_es": "Cultura",
    #     "table": "iepg_data.iepg_final_data_ue",
    #     "column": "culture"},
    # "iepg_ue_information": {
    #     "key": "information",
    #     "precalculus": "eu",
    #     "family": "iepg",
    #     "name_en": "Information",
    #     "name_es": "Información",
    #     "table": "iepg_data.iepg_final_data_ue",
    #     "column": "information"},
    # "iepg_ue_technology": {
    #     "key": "technology",
    #     "precalculus": "eu",
    #     "family": "iepg",
    #     "name_en": "Technology",
    #     "name_es": "Tecnología",
    #     "table": "iepg_data.iepg_final_data_ue",
    #     "column": "technology"},
    # "iepg_ue_science": {
    #     "key": "science",
    #     "precalculus": "eu",
    #     "family": "iepg",
    #     "name_en": "Science",
    #     "name_es": "Ciencia",
    #     "table": "iepg_data.iepg_final_data_ue",
    #     "column": "science"},
    # "iepg_ue_education": {
    #     "key": "education",
    #     "precalculus": "eu",
    #     "family": "iepg",
    #     "name_en": "Education",
    #     "name_es": "Educación",
    #     "table": "iepg_data.iepg_final_data_ue",
    #     "column": "education"},
    # "iepg_ue_cooperation": {
    #     "key": "cooperation",
    #     "precalculus": "eu",
    #     "family": "iepg",
    #     "name_en": "Cooperation",
    #     "name_es": "Cooperación",
    #     "table": "iepg_data.iepg_final_data_ue",
    #     "column": "cooperation"},
    # "iepg_ue_economic_presence": {
    #     "key": "economic_presence",
    #     "precalculus": "eu",
    #     "family": "iepg",
    #     "name_en": "Economic Presence",
    #     "name_es": "Presencia económica",
    #     "table": "iepg_data.iepg_final_data_ue",
    #     "column": "economic_presence"},
    # "iepg_ue_military_presence": {
    #     "key": "military_presence",
    #     "precalculus": "eu",
    #     "family": "iepg",
    #     "name_en": "Military Presence",
    #     "name_es": "Presencia militar",
    #     "table": "iepg_data.iepg_final_data_ue",
    #     "column": "military_presence"},
    # "iepg_ue_soft_presence": {
    #     "key": "soft_presence",
    #     "precalculus": "eu",
    #     "family": "iepg",
    #     "name_en": "Soft Presence",
    #     "name_es": "Presencia blanda",
    #     "table": "iepg_data.iepg_final_data_ue",
    #     "column": "soft_presence"},
    # "iepg_ue": {
    #     "key": "iepg",
    #     "precalculus": "eu",
    #     "family": "iepg",
    #     "name_en": "IEPG",
    #     "name_es": "IEPG",
    #     "table": "iepg_data.iepg_final_data_ue",
    #     "column": "iepg"},
    "population": {
        "key": "population",
        "precalculus": "",
        "family": "context",
        "name_en": "Population",
        "name_es": "Población",
        "table": "iepg_data.pob_pib",
        "column": "population"},
    "gdp": {
        "key": "gdp",
        "precalculus": "",
        "family": "context",
        "name_en": "GDP",
        "name_es": "PIB",
        "table": "iepg_data.pob_pib",
        "column": "pib"}
}
