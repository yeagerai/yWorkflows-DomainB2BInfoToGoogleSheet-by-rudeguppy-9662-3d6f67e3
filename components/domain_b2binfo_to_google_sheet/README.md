
# DomainB2BInfoToGoogleSheet

This Yeager Component takes a domain name as input and retrieves B2B information about the domain. The component then exports the retrieved data to a specified Google Sheet. The input DomainNameInputModel takes a domain name string as input. The output GoogleSheetOutputModel will return the URL of the Google Sheet containing the B2B information.

## Initial generation prompt
description: 'IOs - input: ''DomainNameInputModel(domain: str)''

  output: ''GoogleSheetOutputModel(sheet_url: str)''

  '
name: DomainB2BInfoToGoogleSheet


## Transformer breakdown
- Retrieve the B2B information for the given domain.
- Create a new Google Sheet.
- Export the B2B information to the newly created Google Sheet.
- Return the URL of the Google Sheet containing the B2B information.

## Parameters
[]

        