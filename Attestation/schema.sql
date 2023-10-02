/* (Beta) Export of data model Attestation of the subject dataModel.VerifiableCredentials for a PostgreSQL database. Pending translation of enumerations and multityped attributes */

CREATE TABLE Attestation (credentialSchema JSON, credentialStatus JSON, credentialSubject JSON, evidence JSON, expirationDate TIMESTAMP, id TEXT, issuanceDate TIMESTAMP, issued TIMESTAMP, issuer TEXT, proof JSON, type JSON, validFrom TIMESTAMP, validUntil TIMESTAMP);