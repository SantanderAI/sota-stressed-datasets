# Codebook — Attribute codes

Mapping of the raw attribute codes used in `value.json_view` to their human-readable
meaning. Inherited from the original German Credit dataset. 20 attributes total:
7 numeric, 13 categorical.

## Numeric attributes

| Field | Meaning |
|-------|---------|
| `duration` | Credit duration (months) |
| `credit_amount` | Credit amount (DM) |
| `installment_rate` | Installment rate (% of disposable income) |
| `residence_since` | Residence duration (years) |
| `age` | Age (years) |
| `num_existing_credits` | Number of existing credits at this bank |
| `num_dependents` | Number of dependents |

## Categorical attributes

### `checking_account` — Checking account status
| Code | Meaning |
|------|---------|
| `A11` | < 0 DM |
| `A12` | 0 <= ... < 200 DM |
| `A13` | >= 200 DM / salary assignments for at least 1 year |
| `A14` | no checking account |

### `credit_history` — Credit history
| Code | Meaning |
|------|---------|
| `A30` | no credits taken / all credits paid back duly |
| `A31` | all credits at this bank paid back duly |
| `A32` | existing credits paid back duly till now |
| `A33` | delay in paying off in the past |
| `A34` | critical account / other credits existing (not at this bank) |

### `purpose` — Purpose of credit
| Code | Meaning |
|------|---------|
| `A40` | car (new) |
| `A41` | car (used) |
| `A42` | furniture/equipment |
| `A43` | radio/television |
| `A44` | domestic appliances |
| `A45` | repairs |
| `A46` | education |
| `A47` | vacation |
| `A48` | retraining |
| `A49` | business |
| `A410` | others |

### `savings_account` — Savings account
| Code | Meaning |
|------|---------|
| `A61` | < 100 DM |
| `A62` | 100 <= ... < 500 DM |
| `A63` | 500 <= ... < 1000 DM |
| `A64` | >= 1000 DM |
| `A65` | unknown / no savings account |

### `employment_since` — Employment duration
| Code | Meaning |
|------|---------|
| `A71` | unemployed |
| `A72` | < 1 year |
| `A73` | 1 <= ... < 4 years |
| `A74` | 4 <= ... < 7 years |
| `A75` | >= 7 years |

### `personal_status_sex` — Personal status and sex
| Code | Meaning |
|------|---------|
| `A91` | male : divorced/separated |
| `A92` | female : divorced/separated/married |
| `A93` | male : single |
| `A94` | male : married/widowed |
| `A95` | female : single |

### `other_debtors` — Other debtors / guarantors
| Code | Meaning |
|------|---------|
| `A101` | none |
| `A102` | co-applicant |
| `A103` | guarantor |

### `property` — Property
| Code | Meaning |
|------|---------|
| `A121` | real estate |
| `A122` | building society savings agreement / life insurance |
| `A123` | car or other |
| `A124` | unknown / no property |

### `other_installment_plans` — Other installment plans
| Code | Meaning |
|------|---------|
| `A141` | bank |
| `A142` | stores |
| `A143` | none |

### `housing` — Housing
| Code | Meaning |
|------|---------|
| `A151` | rent |
| `A152` | own |
| `A153` | for free |

### `job` — Job
| Code | Meaning |
|------|---------|
| `A171` | unemployed / unskilled - non-resident |
| `A172` | unskilled - resident |
| `A173` | skilled employee / official |
| `A174` | management / self-employed / highly qualified employee / officer |

### `telephone` — Telephone
| Code | Meaning |
|------|---------|
| `A191` | none |
| `A192` | yes, registered under the customer's name |

### `foreign_worker` — Foreign worker
| Code | Meaning |
|------|---------|
| `A201` | yes |
| `A202` | no |
