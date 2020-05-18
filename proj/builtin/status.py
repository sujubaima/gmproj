class PersonAddSkillNode(SkillNode):
    """
    允许角色习得某技能
    """
    def learn(self, person):
        skill = Skill.one(self.skill)
        if skill.belongs is None:
            skill.belongs = self.belongs
        person.skills.append(skill)


class PersonChangeAttributeNode(SkillNode):
    """
    修改角色属性
    """
    def learn(self, person):
        for attr in self.attrs:
            attrname = attr["name"]
            delta = attr["delta"]
            oldattr = getattr(person, attrname)
            newattr = oldattr + delta
            setattr(person, attrname, newattr)


class SkillChangeAttributeNode(SkillNode):
    """
    修改技能属性
    """
    def learn(self, person):
        for s in person.skills:
            if s.tpl_id == self.skill_id:
                skill = s
                break
        for attr in self.attrs:
            attrname = attr["name"]
            delta = attr["delta"]
            oldattr = getattr(skill, attrname)
            newattr = oldattr + delta
            setattr(skill, attrname, newattr)
