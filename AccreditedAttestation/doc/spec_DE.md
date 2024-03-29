<!-- 10-Header -->  
[![Smart Data Models](https://smartdatamodels.org/wp-content/uploads/2022/01/SmartDataModels_logo.png "Logo")](https://smartdatamodels.org)  
Einrichtung: AkkreditiertAttestation  
====================================<!-- /10-Header -->  
<!-- 15-License -->  
[Offene Lizenz](https://github.com/smart-data-models//dataModel.VerifiableCredentials/blob/master/AccreditedAttestation/LICENSE.md)  
[Dokument automatisch generiert](https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)  
<!-- /15-License -->  
<!-- 20-Description -->  
Globale Beschreibung: **Schema einer EBSI-akkreditierten überprüfbaren Bescheinigung**  
Version: 0.0.1  
<!-- /20-Description -->  
<!-- 30-PropertiesList -->  

## Liste der Eigenschaften  

<sup><sub>[*] Wenn es für ein Attribut keinen Typ gibt, kann es mehrere Typen oder verschiedene Formate/Muster haben</sub></sup>.  
- `credentialSchema[object]`: Enthält Informationen über das Berechtigungsschema (Vorlage), auf dem die überprüfbare Berechtigung basiert  	- `id[uri]`: Verweist auf das im (relevanten) Register der vertrauenswürdigen Schemata (TSR) gespeicherte Berechtigungsschema (Vorlage), auf dem die überprüfbare Berechtigung beruht    
- `credentialStatus[object]`: Enthält Informationen darüber, wie der Status der überprüfbaren Bescheinigung überprüft werden kann (über das Register für Widerrufe und Bestätigungen, RER)  	- `id[uri]`: Referenzdatensatz im Register für Widerrufe und Vermerke (RER) zur Überprüfung der Gültigkeit einer überprüfbaren Bescheinigung    
	- `statusListCredential[uri]`: URL, die auf die StatusList2021Credential verweist    
	- `statusListIndex[string]`: Ganzzahl, ausgedrückt als Zeichenkette. Der auf Null basierende Indexwert identifiziert die Bitposition des Status    
	- `statusPurpose[string]`: Zweck des Statuseintrags    
- `credentialSubject[object]`: Definiert Informationen über das Subjekt, das durch die überprüfbare Bescheinigung beschrieben wird  	  
- `evidence[array]`: Enthält Informationen über den Prozess, der zur Ausstellung der überprüfbaren Bescheinigung geführt hat  - `expirationDate[date-time]`: Legt das Datum und die Uhrzeit fest, zu der die überprüfbare Bescheinigung abläuft  - `id[uri]`: Definiert den eindeutigen Bezeichner der überprüfbaren Bescheinigung  - `issuanceDate[date-time]`: Legt das Datum und die Uhrzeit fest, zu der die überprüfbare Bescheinigung gültig wird  - `issued[date-time]`: Legt fest, wann die überprüfbare Bescheinigung ausgestellt wurde  - `issuer[uri]`: Legt den Aussteller der prüfbaren Bescheinigung fest  - `proof[object]`: Enthält Informationen über den Nachweis  	- `created[date-time]`: Legt das Datum und die Uhrzeit fest, wann der Proof erstellt wurde    
	- `jws[string]`: Definiert den Proof-Wert im JWS-Format    
	- `proofPurpose[string]`: Definiert den Zweck des Nachweises    
	- `type[string]`: Definiert den Beweistyp    
- `termsOfUse[array]`: Enthält die Bedingungen, unter denen die akkreditierte überprüfbare Bescheinigung ausgestellt wurde  - `type[array]`: Definiert den Typ der überprüfbaren Bescheinigung  - `validFrom[date-time]`: Legt das Datum und die Uhrzeit fest, zu der die überprüfbare Bescheinigung gültig wird  - `validUntil[date-time]`: Legt das Datum und die Uhrzeit fest, zu der die überprüfbare Bescheinigung abläuft  <!-- /30-PropertiesList -->  
<!-- 35-RequiredProperties -->  
Erforderliche Eigenschaften  
<!-- /35-RequiredProperties -->  
<!-- 40-RequiredProperties -->  
Datenmodelle, die von EBSI-Json-Schemata abgeleitet sind https://ec.europa.eu/digital-building-blocks/code/projects/EBSI/repos/json-schema/browse/schemas. Das Attribut @context wurde aus der Definition entfernt, da es in NGSI-LD obligatorisch ist und nicht explizit dokumentiert werden muss. Nur das Beispiel in Key Values Linked Data verfügbar  
<!-- /40-RequiredProperties -->  
<!-- 50-DataModelHeader -->  
## Datenmodell Beschreibung der Eigenschaften  
Alphabetisch sortiert (für Details anklicken)  
<!-- /50-DataModelHeader -->  
<!-- 60-ModelYaml -->  
<details><summary><strong>full yaml details</strong></summary>    
```yaml  
AccreditedAttestation:    
  description: Schema of an EBSI Accredited Verifiable Attestation    
  properties:    
    credentialSchema:    
      description: Contains information about the credential schema (template) on which the Verifiable Authorisation is based    
      properties:    
        id:    
          description: References the credential schema (template) stored on the (relevant) Trusted Schemas Registry (TSR) on which the Verifiable Authorisation is based    
          format: uri    
          type: string    
          x-ngsi:    
            type: Property    
        type:    
          description: Defines credential schema type    
          enum:    
            - FullJsonSchemaValidator2021    
          type: string    
          x-ngsi:    
            type: Property    
      required:    
        - id    
        - type    
      type: object    
      x-ngsi:    
        type: Property    
    credentialStatus:    
      description: 'Contains information about how to verify the status of the Verifiable Attestation (via the Revocation and Endorsement Registry, RER)'    
      properties:    
        id:    
          description: References record in the Revocation and Endorsement Registry (RER) to enable verification of a Verifiable Attestation’s validity    
          format: uri    
          type: string    
          x-ngsi:    
            type: Property    
        statusListCredential:    
          description: URL referencing the StatusList2021Credential    
          format: uri    
          type: string    
          x-ngsi:    
            type: Property    
        statusListIndex:    
          description: Integer expressed as a string. The zero based index value identifies the bit position of the status    
          type: string    
          x-ngsi:    
            type: Property    
        statusPurpose:    
          description: Purpose of the status entry    
          enum:    
            - revocation    
            - suspension    
          type: string    
          x-ngsi:    
            type: Property    
        type:    
          description: Defines the Verifiable Credential status type    
          type: string    
          x-ngsi:    
            type: Property    
      required:    
        - id    
        - type    
      type: object    
      x-ngsi:    
        type: Property    
    credentialSubject:    
      description: Defines information about the subject that is described by the Verifiable Attestation    
      properties:    
        id:    
          description: Defines the DID of the subject that is described by the Verifiable Attestation    
          format: uri    
          type: string    
          x-ngsi:    
            type: Property    
      type: object    
      x-ngsi:    
        type: Property    
    evidence:    
      description: Contains information about the process which resulted in the issuance of the Verifiable Attestation    
      items:    
        properties:    
          documentPresence:    
            items:    
              description: Description to be completed    
              type: string    
              x-ngsi:    
                type: Property    
            type: array    
          evidenceDocument:    
            items:    
              description: Description to be completed    
              type: string    
              x-ngsi:    
                type: Property    
            type: array    
          id:    
            description: 'If present, it MUST contain a URL that points to where more information about this instance of evidence can be found'    
            type: string    
            x-ngsi:    
              type: Property    
          subjectPresence:    
            description: Description to be completed    
            type: string    
            x-ngsi:    
              type: Property    
          type:    
            description: Defines the evidence type    
            items:    
              type: string    
            type: array    
            x-ngsi:    
              type: Property    
        required:    
          - id    
          - type    
        type: object    
      type: array    
      x-ngsi:    
        type: Property    
    expirationDate:    
      description: 'Defines the date and time, when the Verifiable Attestation expires'    
      format: date-time    
      type: string    
      x-ngsi:    
        type: Property    
    id:    
      description: Defines unique identifier of the Verifiable Attestation    
      format: uri    
      type: string    
      x-ngsi:    
        type: Property    
    issuanceDate:    
      description: 'Defines the date and time, when the Verifiable Attestation becomes valid'    
      format: date-time    
      type: string    
      x-ngsi:    
        type: Property    
    issued:    
      description: Defines when the Verifiable Attestation was issued    
      format: date-time    
      type: string    
      x-ngsi:    
        type: Property    
    issuer:    
      description: Defines the issuer of the Verifiable Attestation    
      format: uri    
      type: string    
      x-ngsi:    
        type: Property    
    proof:    
      description: Contains information about the proof    
      properties:    
        created:    
          description: 'Defines the date and time, when the proof has been created'    
          format: date-time    
          type: string    
          x-ngsi:    
            type: Property    
        jws:    
          description: Defines the proof value in JWS format    
          type: string    
          x-ngsi:    
            type: Property    
        proofPurpose:    
          description: Defines the purpose of the proof    
          type: string    
          x-ngsi:    
            type: Property    
        type:    
          description: Defines the proof type    
          type: string    
          x-ngsi:    
            type: Property    
        verificationMethod:    
          description: Contains information about the verification method / proof mechanisms    
          type: string    
          x-ngsi:    
            type: Property    
      required:    
        - type    
        - proofPurpose    
        - created    
        - verificationMethod    
        - jws    
      type: object    
      x-ngsi:    
        type: Property    
    termsOfUse:    
      description: Contains the terms under which the Accredited Verifiable Attestation was issued    
      items:    
        description: Description to be completed    
        properties:    
          id:    
            description: Contains a URL that points to where more information about this instance of terms of use can be found    
            format: uri    
            type: string    
            x-ngsi:    
              type: Property    
          type:    
            description: Defines the type of terms of use    
            type: string    
            x-ngsi:    
              type: Property    
        required:    
          - id    
          - type    
        type: object    
        x-ngsi:    
          type: Property    
      type: array    
      x-ngsi:    
        type: Property    
    type:    
      description: Defines the Verifiable Credential type    
      items:    
        type: string    
      type: array    
      x-ngsi:    
        type: Property    
    validFrom:    
      description: 'Defines the date and time, when the Verifiable Attestation becomes valid'    
      format: date-time    
      type: string    
      x-ngsi:    
        type: Property    
    validUntil:    
      description: 'Defines the date and time, when the Verifiable Attestation expires'    
      format: date-time    
      type: string    
      x-ngsi:    
        type: Property    
  required: []    
  type: object    
  x-derived-from: https://ec.europa.eu/digital-building-blocks/code/projects/EBSI/repos/json-schema/browse/schemas/ebsi-accredited-attestation/2022-11/schema.json    
  x-disclaimer: 'Redistribution and use in source and binary forms, with or without modification, are permitted  provided that the license conditions are met. Copyleft (c) 2022 Contributors to Smart Data Models Program'    
  x-license-url: https://github.com/smart-data-models/dataModel.VerifiableCredentials/blob/master/AccreditedAttestation/LICENSE.md    
  x-model-schema: ""    
  x-model-tags: 'EBSI, Verifiable Credentials'    
  x-version: 0.0.1    
```  
</details>    
<!-- /60-ModelYaml -->  
<!-- 70-MiddleNotes -->  
<!-- /70-MiddleNotes -->  
<!-- 80-Examples -->  
## Beispiel-Nutzlasten  
Nicht verfügbar ist das Beispiel einer AccreditedAttestation im JSON-LD-Format als Key-Values. Dies ist kompatibel mit NGSI-v2, wenn `options=keyValues` verwendet wird und liefert die Kontextdaten einer einzelnen Entität.  
Nicht verfügbar ist das Beispiel einer AccreditedAttestation im JSON-LD-Format in normalisierter Form. Dies ist kompatibel mit NGSI-v2, wenn keine Optionen verwendet werden, und liefert die Kontextdaten einer einzelnen Entität.  
#### AccreditedAttestation NGSI-LD key-values Beispiel  
Hier ist ein Beispiel für eine AccreditedAttestation im JSON-LD-Format als Key-Values. Dies ist mit NGSI-LD kompatibel, wenn `options=keyValues` verwendet wird und liefert die Kontextdaten einer einzelnen Entität.  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
  "@context": ["https://www.w3.org/2018/credentials/v1"],  
  "id": "urn:uuid:58afcb57-81f9-4e8c-817b-01f0597d6801",  
  "type": [  
    "VerifiableCredential",  
    "VerifiableAttestation",  
    "AccreditedVerifiableAttestation"  
  ],  
  "issuer": "did:ebsi:00001234",  
  "issuanceDate": "2021-11-01T00:00:00Z",  
  "validFrom": "2021-11-01T00:00:00Z",  
  "expirationDate": "2024-06-22T14:11:44Z",  
  "issued": "2020-06-22T14:11:44Z",  
  "termsOfUse": [  
    {  
      "id": "https://essif.europa.eu/accreditation/45",  
      "type": "VerifiableAccreditation"  
    }  
  ],  
  "credentialSubject": {  
    "id": "did:ebsi:00001235"  
  },  
  "credentialStatus": {  
    "id": "https://essif.europa.eu/status/45",  
    "type": "CredentialsStatusList2020"  
  },  
  "credentialSchema": {  
    "id": "https://api-test.ebsi.eu/trusted-schemas-registry/v2/schemas/0x4a131e78474b35ca4c93d4904cae9f2013cd53794ce521f6fcfac17ac460c6e5",  
    "type": "FullJsonSchemaValidator2021"  
  }  
}  
```  
</details>  
Nicht verfügbar ist das Beispiel einer AccreditedAttestation im JSON-LD-Format in normalisierter Form. Dies ist kompatibel mit NGSI-LD, wenn keine Optionen verwendet werden, und liefert die Kontextdaten einer einzelnen Entität.  
<!-- /80-Examples -->  
<!-- 90-FooterNotes -->  
<!-- /90-FooterNotes -->  
<!-- 95-Units -->  
Siehe [FAQ 10] (https://smartdatamodels.org/index.php/faqs/), um eine Antwort auf die Frage zu erhalten, wie man mit Größeneinheiten umgeht  
<!-- /95-Units -->  
<!-- 97-LastFooter -->  
---  
[Smart Data Models](https://smartdatamodels.org) +++ [Contribution Manual](https://bit.ly/contribution_manual) +++ [About](https://bit.ly/Introduction_SDM)<!-- /97-LastFooter -->  
