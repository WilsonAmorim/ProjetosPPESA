CREATE TABLE `sys`.`tbconvenio` (
    `idtbConvenio` INT(11) NOT NULL AUTO_INCREMENT,
    `tbConvenioLote` VARCHAR(45) NOT NULL,
    PRIMARY KEY (`idtbConvenio`)
) ENGINE = InnoDB DEFAULT CHARACTER SET = utf8mb4 COLLATE = utf8mb4_general_ci COMMENT = 'Tabela de convencio';