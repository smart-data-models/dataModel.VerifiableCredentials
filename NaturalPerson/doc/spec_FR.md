<!-- 10-Header -->  
[![Smart Data Models](https://smartdatamodels.org/wp-content/uploads/2022/01/SmartDataModels_logo.png "Logo")](https://smartdatamodels.org)  
Entité : PersonneNaturelle  
==========================<!-- /10-Header -->  
<!-- 15-License -->  
[Licence ouverte] (https://github.com/smart-data-models//dataModel.VerifiableCredentials/blob/master/NaturalPerson/LICENSE.md)  
[document généré automatiquement] (https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)  
<!-- /15-License -->  
<!-- 20-Description -->  
Description globale : **Schéma d'un identifiant vérifiable EBSI pour une personne physique**  
version : 0.0.1  
<!-- /20-Description -->  
<!-- 30-PropertiesList -->  

## Liste des propriétés  

<sup><sub>[*] S'il n'y a pas de type dans un attribut, c'est parce qu'il peut avoir plusieurs types ou différents formats/modèles</sub></sup>.  
- `credentialSchema[object]`: Contient des informations sur le schéma d'identification (modèle) sur lequel l'autorisation vérifiable est basée.  	- `id[uri]`: Fait référence au schéma (modèle) d'identification stocké dans le registre (pertinent) des schémas de confiance (TSR) sur lequel l'autorisation vérifiable est basée.    
- `credentialStatus[object]`: Contient des informations sur la manière de vérifier le statut de l'attestation vérifiable (via le registre de révocation et d'endossement, RER).  	- `id[uri]`: Enregistrement de références dans le registre de révocation et d'endossement (RER) pour permettre la vérification de la validité d'une attestation vérifiable.    
	- `statusListCredential[uri]`: URL faisant référence à l'identifiant StatusList2021Credential    
	- `statusListIndex[string]`: Entier exprimé sous forme de chaîne de caractères. La valeur d'index basée sur zéro identifie la position du bit de l'état.    
	- `statusPurpose[string]`: Objet de l'entrée de statut    
- `credentialSubject[object]`: Définit des informations supplémentaires sur le sujet qui est décrit par l'identifiant vérifiable.  	- `currentAddress[string]`: Définit l'adresse actuelle du sujet de la lettre de créance.    
	- `dateOfBirth[date]`: Définit la date de naissance du sujet de la lettre de créance.    
	- `familyName[string]`: Définit le(s) nom(s) de famille actuel(s) du sujet de la lettre de créance.    
	- `firstName[string]`: Définit le(s) prénom(s) actuel(s) du sujet de la lettre de créance    
	- `gender[string]`: Définit le sexe du sujet de la lettre de créance.    
	- `id[uri]`: Définit le DID du sujet qui est décrit par l'attestation vérifiable.    
	- `nameAndFamilyNameAtBirth[string]`: Définit le prénom et le(s) nom(s) de famille de la personne concernée au moment de sa naissance.    
	- `personalIdentifier[string]`: Définit l'identifiant national unique de la personne concernée (construit par l'État membre d'envoi conformément aux spécifications techniques aux fins de l'identification transfrontalière et qui est aussi persistant que possible dans le temps).    
- `evidence[array]`: Contient des informations sur le processus qui a abouti à la délivrance de l'attestation vérifiable.  - `expirationDate[date-time]`: Définit la date et l'heure d'expiration de l'attestation vérifiable.  - `id[uri]`: Définit l'identifiant unique de l'attestation vérifiable.  - `issuanceDate[date-time]`: Définit la date et l'heure auxquelles l'attestation vérifiable devient valide.  - `issued[date-time]`: Définit la date à laquelle l'attestation vérifiable a été délivrée.  - `issuer[uri]`: Définit l'émetteur de l'attestation vérifiable  - `proof[object]`: Contient des informations sur la preuve  	- `created[date-time]`: Définit la date et l'heure auxquelles l'épreuve a été créée.    
	- `jws[string]`: Définit la valeur de la preuve au format JWS    
	- `proofPurpose[string]`: Définit l'objectif de la preuve    
	- `type[string]`: Définit le type de preuve    
- `type[array]`: Définit le type de justificatif vérifiable  - `validFrom[date-time]`: Définit la date et l'heure auxquelles l'attestation vérifiable devient valide.  - `validUntil[date-time]`: Définit la date et l'heure d'expiration de l'attestation vérifiable.  <!-- /30-PropertiesList -->  
<!-- 35-RequiredProperties -->  
Propriétés requises  
- `credentialSubject`  <!-- /35-RequiredProperties -->  
<!-- 40-RequiredProperties -->  
Modèles de données dérivés des schémas json des EBSI https://ec.europa.eu/digital-building-blocks/code/projects/EBSI/repos/json-schema/browse/schemas. L'attribut @context a été supprimé de la définition car il est obligatoire dans la NGSI-LD et n'a pas besoin d'être documenté explicitement. Seul l'exemple des données liées aux valeurs clés est disponible  
<!-- /40-RequiredProperties -->  
<!-- 50-DataModelHeader -->  
## Modèle de données description des propriétés  
Classés par ordre alphabétique (cliquez pour plus de détails)  
<!-- /50-DataModelHeader -->  
<!-- 60-ModelYaml -->  
<details><summary><strong>full yaml details</strong></summary>    
```yaml  
NaturalPerson:    
  description: Schema of an EBSI Verifiable ID for a natural person    
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
      description: Defines additional information about the subject that is described by the Verifiable ID    
      properties:    
        currentAddress:    
          description: Defines the current address of the credential subject    
          type: string    
          x-ngsi:    
            type: Property    
        dateOfBirth:    
          description: Defines date of birth of the credential subject    
          format: date    
          type: string    
          x-ngsi:    
            type: Property    
        familyName:    
          description: Defines current family name(s) of the credential subject    
          type: string    
          x-ngsi:    
            type: Property    
        firstName:    
          description: Defines current first name(s) of the credential subject    
          type: string    
          x-ngsi:    
            type: Property    
        gender:    
          description: Defines the gender of the credential subject    
          type: string    
          x-ngsi:    
            type: Property    
        id:    
          description: Defines the DID of the subject that is described by the Verifiable Attestation    
          format: uri    
          type: string    
          x-ngsi:    
            type: Property    
        nameAndFamilyNameAtBirth:    
          description: Defines the first and the family name(s) of the credential subject at the time of their birth    
          type: string    
          x-ngsi:    
            type: Property    
        personalIdentifier:    
          description: Defines the unique national identifier of the credential subject (constructed by the sending Member State in accordance with the technical specifications for the purposes of cross-border identification and which is as persistent as possible in time)    
          type: string    
          x-ngsi:    
            type: Property    
        placeOfBirth:    
          description: Defines the place where the credential subjectis born    
          type: string    
          x-ngsi:    
            type: Property    
      required:    
        - id    
        - familyName    
        - firstName    
        - dateOfBirth    
        - personalIdentifier    
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
  required:    
    - credentialSubject    
  type: object    
  x-derived-from: https://ec.europa.eu/digital-building-blocks/code/projects/EBSI/repos/json-schema/browse/schemas/ebsi-vid/natural-person/2022-11/schema.json    
  x-disclaimer: 'Redistribution and use in source and binary forms, with or without modification, are permitted  provided that the license conditions are met. Copyleft (c) 2022 Contributors to Smart Data Models Program'    
  x-license-url: https://github.com/smart-data-models/dataModel.VerifiableCredentials/blob/master/NaturalPerson/LICENSE.md    
  x-model-schema: ""    
  x-model-tags: 'EBSI, Verifiable Credentials'    
  x-version: 0.0.1    
```  
</details>    
<!-- /60-ModelYaml -->  
<!-- 70-MiddleNotes -->  
<!-- /70-MiddleNotes -->  
<!-- 80-Examples -->  
## Exemples de charges utiles  
Non disponible l'exemple d'une NaturalPerson au format JSON-LD en tant que valeurs clés. Ceci est compatible avec NGSI-v2 lorsque l'on utilise `options=keyValues` et renvoie les données de contexte d'une entité individuelle.  
Non disponible l'exemple d'une NaturalPerson au format JSON-LD tel que normalisé. Ce format est compatible avec l'INSG-v2 lorsqu'il n'utilise pas d'options et renvoie les données contextuelles d'une entité individuelle.  
#### NaturalPerson Valeurs clés de l'INS-LD Exemple  
Voici un exemple de NaturalPerson au format JSON-LD en tant que valeurs clés. Ceci est compatible avec NGSI-LD lorsque l'on utilise `options=keyValues` et renvoie les données contextuelles d'une entité individuelle.  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
  "@context": ["https://www.w3.org/2018/credentials/v1"],  
  "id": "urn:did:123456",  
  "type": ["VerifiableCredential", "VerifiableAttestation", "VerifiableId"],  
  "issuer": "urn:did:9999999",  
  "issuanceDate": "2021-11-01T00:00:00Z",  
  "validFrom": "2021-11-01T00:00:00Z",  
  "issued": "2021-11-01T00:00:00Z",  
  "credentialSubject": {  
    "id": "urn:uri:123",  
    "personalIdentifier": "IT/DE/1234",  
    "familyName": "Castafiori",  
    "firstName": "Bianca",  
    "dateOfBirth": "1930-10-01"  
  },  
  "credentialSchema": {  
    "id": "https://permanent.url.of/vid/naturalperson",  
    "type": "FullJsonSchemaValidator2021"  
  }  
}  
```  
</details>  
Non disponible l'exemple d'une NaturalPerson au format JSON-LD tel que normalisé. Ce format est compatible avec NGSI-LD lorsque les options ne sont pas utilisées et renvoie les données contextuelles d'une entité individuelle.  
<!-- /80-Examples -->  
<!-- 90-FooterNotes -->  
<!-- /90-FooterNotes -->  
<!-- 95-Units -->  
Voir [FAQ 10] (https://smartdatamodels.org/index.php/faqs/) pour obtenir une réponse à la question de savoir comment traiter les unités de magnitude.  
<!-- /95-Units -->  
<!-- 97-LastFooter -->  
---  
[Smart Data Models](https://smartdatamodels.org) +++ [Contribution Manual](https://bit.ly/contribution_manual) +++ [About](https://bit.ly/Introduction_SDM)<!-- /97-LastFooter -->  
