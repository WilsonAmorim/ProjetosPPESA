CREATE TABLE `ppeconecao`.`tborgaos` (
  `idtborgaos` INT NOT NULL AUTO_INCREMENT,
  `Sigla` VARCHAR(45),
  `tborgaosidtbConvenio` INT NOT NULL,
  `tbOrgaosDescricao` VARCHAR(100) NOT NULL,
  PRIMARY KEY (`idtborgaos`, `tborgaosidtbConvenio`),
  UNIQUE INDEX `idtborgaos_UNIQUE` (`idtborgaos` ASC) VISIBLE)
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_general_ci
COMMENT = 'Tabela de orgaos conveniados';